from microbit import *
import utime
import math
from Button import Button
from wukong import *

class Sima:
    def __init__(self, x0, y0, firstAngle, xf, yf, v, angularVelocity, lin_regulation, ang_regulation, HC_SR04_pin, panic_pin):
        self.x = x0
        self.y = y0
        self.x0 = x0
        self.y0 = y0
        self.theta = firstAngle
        self.xf = xf
        self.yf = yf
        self.v = v
        self.angularVelocity = angularVelocity
        self.lin_regulation = lin_regulation
        self.ang_regulation = ang_regulation
        self.HC_SR04_pin = HC_SR04_pin
        self.wk = WUKONG()
        self.emergencyBtn = Button(panic_pin)
        
        # ✅ VARIABLES ODOMETRÍA COMO ATRIBUTOS
        self._last_odom_time = 0.0
        self._last_lin_speed = 0.0
        self._last_ang_speed = 0.0
        
        # ✅ VARIABLES ESQUIVA
        self.stored_trace_point = None
        self.stored_trace_theta = None
        
        # Constantes
        self.ANG_TOL = 0.08
        self.avoid_side = "LEFT"
        self.WAYPOINT_TOLERANCE = 5.0
        self.ULTRASONIC_THRESHOLD = 25
        self.state = "GO_TO_GOAL"

    def setColor(self, color):
        self.color = color
        
    def start(self):
        display.show(Image.ARROW_N)
        # Sistema de arranque
        # TODO: Ignore

        display.show(Image.YES)
        self._last_odom_time = self._current_time()
        while True:
            sleep(10)
            if self.go():
                break

    def go(self):
        if self.emergencyBtn.is_pressed():
            self._stop()
            display.show(Image.NO)
            return True # Break loop principal

        self._update_odometry()
        distance_obst = self._read_ultrasonic()

        if self.state == "GO_TO_GOAL":
            if 0 < distance_obst < self.ULTRASONIC_THRESHOLD:
                # Obstáculo detectado → cambiar a modo esquiva
                self._stop()
                display.show(Image.SAD)
                self.state = "AVOID_OBSTACLE"
            else:
                reached_goal = self._follow_point(self.xf, self.yf)
                if reached_goal:
                    self._stop()
                    display.show(Image.HAPPY)
                    return True # Objetivo alcanzado, salir del loop principal

        elif self.state == "AVOID_OBSTACLE":
            self._avoid_obstacle_maneuver()
            # Tras la maniobra volvemos a navegar hacia el objetivo
            self.state = "GO_TO_GOAL"
            display.show(Image.ARROW_N)

        return False # Continuar el loop principal

    def _read_ultrasonic(self):
        """
        Lee la distancia en centímetros desde el sensor de ultrasonidos.
        Devuelve 0 si no hay objeto detectado (> 400 cm) o hay error.
        """
        return self.wk.read_sonar(self.HC_SR04_pin, 'cm')

    def _set_motor_speeds(self, linear_vel, angular_vel):
        """
        Traduce velocidades lógicas (linear_vel, angular_vel) a señales
        para los dos motores.

        Convenio:
        - linear_vel  > 0  → avance
        - angular_vel > 0  → giro a la izquierda (motor izq más lento)
        - angular_vel < 0  → giro a la derecha   (motor der más lento)

        Los motores están cableados en sentido opuesto, por eso motor 2 va negado.
        Escala los valores al rango -100..100.
        """
        # Calculamos las velocidades de cada rueda
        left_speed  = linear_vel - angular_vel
        right_speed = linear_vel + angular_vel

        # Clamp a [-100, 100]
        left_speed  = max(-100, min(100, int(left_speed)))
        right_speed = max(-100, min(100, int(right_speed)))

        # Motor 1 = izquierdo, Motor 2 = derecho (invertido mecánicamente)
        self.wk.set_motors(1,  left_speed)
        self.wk.set_motors(2, -right_speed)

    def _stop(self):
        """Detiene los dos motores."""
        self.wk.set_motors(1, 0)
        self.wk.set_motors(2, 0)

    def _current_time(self):
        """Tiempo actual en segundos (float)."""
        return utime.ticks_ms() / 1000.0
    
    def _update_odometry(self):
        """
        Integra posición y orientación estimadas a partir del tiempo transcurrido
        y las últimas velocidades aplicadas. Se llama repetidamente en los bucles.
        """
        now = self._current_time()
        dt  = now - self._last_odom_time
        self._last_odom_time = now

        # Avance lineal
        ds = self._last_lin_speed * dt
        self.x += ds * math.cos(self.theta)
        self.y += ds * math.sin(self.theta)
        # Cambio angular
        self.theta += math.radians(self._last_ang_speed * dt)

    def _set_motor_and_track(self, linear_cm_s, angular_deg_s):
        """
        Llama a set_motor_speeds escalando al rango de motores (0-100)
        y registra las velocidades para la odometría.
        """
        self._last_lin_speed  = linear_cm_s
        self._last_ang_speed  = angular_deg_s

        # Escalamos: self.v → LINEAR_SPEED (100% motor)
        lin_m = (linear_cm_s  / self.v) * self.lin_regulation
        ang_m = (angular_deg_s / self.angularVelocity)  * self.ang_regulation
        self._set_motor_speeds(lin_m, ang_m)

    def _dist_2d(self, a_x, a_y, b_x, b_y):
        """Distancia euclidiana entre dos puntos 2D."""
        dx = a_x - b_x
        dy = a_y - b_y
        return math.sqrt(dx*dx + dy*dy)


    def _angle_to_point(self, from_x, from_y, from_theta, to_x, to_y):
        """
        Ángulo que hay que girar para mirar desde (from_x, from_y, from_theta)
        hacia (to_x, to_y). Resultado en [-pi, pi].
        """
        dx = to_x - from_x
        dy = to_y - from_y
        desired = math.atan2(dy, dx)
        error   = desired - from_theta
        # Normalizar a [-pi, pi]
        while error >  math.pi: error -= 2.0 * math.pi
        while error < -math.pi: error += 2.0 * math.pi
        return self._normalize_angle(error)

    def _normalize_angle(self, angle):
        while angle > math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle

    def _project_point_on_main_trace(self, px, py):
        """
        Proyecta (px, py) sobre el segmento start → goal.
        Devuelve (tx, ty), el punto más cercano de la traza.
        """
        vx = self.xf - self.x0
        vy = self.yf - self.y0
        wx = px - self.x0
        wy = py - self.y0
        c2 = vx*vx + vy*vy
        if c2 == 0:
            return self.x0, self.y0
        t = (vx*wx + vy*wy) / c2
        t = max(0.0, min(1.0, t))
        return self.x0 + t*vx, self.y0 + t*vy

    def _follow_point(self, target_x, target_y):
        """
        Avanza hacia (target_x, target_y).
        Primero gira hacia el punto y luego avanza en línea recta.
        Devuelve True cuando llega (dentro de WAYPOINT_TOLERANCE).
        """
        ang_error = self._angle_to_point(self.x, self.y, self.theta, target_x, target_y)
        
        if abs(ang_error) > self.ANG_TOL:
            # Girar hacia el punto
            if ang_error > 0:
                self._set_motor_and_track(0.0,  self.angularVelocity)
            else:
                self._set_motor_and_track(0.0, -self.angularVelocity)
            return False
        else:
            # Avanzar
            self._set_motor_and_track(self.v, 0.0)

        d = self._dist_2d(self.x, self.y, target_x, target_y)
        if d < self.WAYPOINT_TOLERANCE:
            self._stop()
            return True
        return False

    def _follow_point_until_reach(self, tx, ty):
        """
        Bucle que llama a follow_point hasta llegar a (tx, ty).
        Se detiene también si se pulsa el botón de emergencia (button_b).
        """
        while not self.emergencyBtn.is_pressed():
            self._update_odometry()
            if self._follow_point(tx, ty):
                break

    def _turn_angle(self, angle_degrees):
        """
        Gira el robot exactamente 'angle_degrees' grados usando tiempo.
        Positivo = izquierda, Negativo = derecha.
        Actualiza theta.
        """
        if angle_degrees == 0:
            return

        direction = 1 if angle_degrees > 0 else -1
        self._set_motor_and_track(0.0, direction * self.angularVelocity)

        t_needed = abs(angle_degrees) / self.angularVelocity   # segundos
        t_start  = self._current_time()
        while self._current_time() - t_start < t_needed:
            self._update_odometry()
            if self.emergencyBtn.is_pressed():
                break

        self._stop()
        self.theta += math.radians(angle_degrees)
        # Normalizar theta a [-pi, pi]
        while self.theta >  math.pi: self.theta -= 2.0 * math.pi
        while self.theta < -math.pi: self.theta += 2.0 * math.pi
        self._last_lin_speed_reset()

    def _move_straight(self, distance_cm):
        """
        Avanza en línea recta 'distance_cm' centímetros usando tiempo.
        """
        self._set_motor_and_track(self.v, 0.0)

        t_needed = distance_cm / self.v   # segundos
        t_start  = self._current_time()
        while self._current_time() - t_start < t_needed:
            self._update_odometry()
            if self.emergencyBtn.is_pressed():
                break
        self._stop()
        self._last_lin_speed_reset()

    def _last_lin_speed_reset(self):
        """Resetea la velocidad interna tras una parada."""
        self._last_lin_speed = 0.0
        self._last_ang_speed = 0.0

    def _turn_to_orientation(self, target_theta):
        """
        Gira hasta alcanzar una orientación absoluta target_theta (radianes).
        """
        while not self.emergencyBtn.is_pressed():
            self._update_odometry()
            error = target_theta - self.theta
            # Normalizar a [-pi, pi]
            while error >  math.pi: error -= 2.0 * math.pi
            while error < -math.pi: error += 2.0 * math.pi

            if abs(error) < 0.05:
                self._stop()
                self._last_lin_speed_reset()
                break
            else:
                if error > 0:
                    self._set_motor_and_track(0.0,  self.angularVelocity)
                else:
                    self._set_motor_and_track(0.0, -self.angularVelocity)

    def _avoid_obstacle_maneuver(self):
        """
        Maniobra en U para rodear un obstáculo y volver a la traza:
        1. Guarda el punto actual proyectado sobre la traza y la orientación.
        2. Gira 90° hacia el lado de esquiva.
        3. Avanza lateralmente para apartarse del obstáculo.
        4. Gira 90° de vuelta a la dirección original.
        5. Avanza para sobrepasar el obstáculo en longitud.
        6. Gira 90° hacia la traza.
        7. Avanza hasta la proyección guardada en la traza.
        8. Gira para recuperar la orientación original.
        """
        # 1) Guardar punto y orientación de la traza
        self.stored_trace_point = self._project_point_on_main_trace(self.x, self.y)
        self.stored_trace_theta = self.theta

        # Distancias de maniobra — ajusta según el tamaño real del robot y el obstáculo
        lateral_distance = 30.0   # cm de apartado lateral
        forward_distance = 50.0   # cm de avance para sobrepasar

        side_sign = +1 if self.avoid_side == "LEFT" else -1

        # 2) Girar 90° hacia el lado de esquiva
        self._turn_angle(90.0 * side_sign)

        # 3) Avanzar lateralmente
        self._move_straight(lateral_distance)

        # 4) Girar 90° de vuelta a la dirección de avance original
        self._turn_angle(-90.0 * side_sign)

        # 5) Avanzar para pasar el obstáculo
        self._move_straight(forward_distance)

        # 6) Girar 90° hacia la traza (hacia el interior)
        self._turn_angle(-90.0 * side_sign)

        # 7) Avanzar hasta la proyección de la traza
        target_x, target_y = self.stored_trace_point
        self._follow_point_until_reach(target_x, target_y)

        # 8) Recuperar orientación original
        self._turn_to_orientation(self.stored_trace_theta)