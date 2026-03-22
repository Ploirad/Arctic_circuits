from microbit import *
import utime
import math
from wukong import *

wk = WUKONG()

###########################################
# CONFIGURACIÓN INICIAL
###########################################

# Pose del robot (se actualiza con odometría por tiempo)
x, y   = 0.0, 0.0   # posición inicial (cm)
theta  = 0.0         # orientación inicial (radianes)

# Punto de inicio (para proyecciones sobre la traza)
start_x, start_y = x, y

# Objetivo global (en centímetros)
goal_x, goal_y = 100.0, 0.0   # cambia este punto según la competición

# Parámetros de control
LINEAR_SPEED       = 60     # velocidad lineal motores (0-100)
ANGULAR_SPEED      = 30     # velocidad angular motores (0-100)
LINEAR_SPEED_CM_S  = 15.0   # velocidad lineal estimada en cm/s (calibrar)
ANG_SPEED_DEG_S    = 90.0   # velocidad angular estimada en deg/s (calibrar)

ULTRASONIC_THRESHOLD = 25   # cm — distancia mínima para detectar obstáculo
WAYPOINT_TOLERANCE   = 5.0  # cm — tolerancia para considerar que se llegó al punto

# Estado principal
state = "GO_TO_GOAL"   # "GO_TO_GOAL" | "AVOID_OBSTACLE"

# Variables de esquiva
stored_trace_point = None
stored_trace_theta = None
avoid_side         = "LEFT"   # "LEFT" | "RIGHT"

# Pin del ultrasonidos (ajusta según tu cableado en la Wukong)
SONAR_PIN = pin0


###########################################
# FUNCIONES DE HARDWARE
###########################################

def read_ultrasonic():
    """
    Lee la distancia en centímetros desde el sensor de ultrasonidos.
    Devuelve 0 si no hay objeto detectado (> 400 cm) o hay error.
    """
    return wk.read_sonar(SONAR_PIN, 'cm')


def set_motor_speeds(linear_vel, angular_vel):
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
    wk.set_motors(1,  left_speed)
    wk.set_motors(2, -right_speed)


def Parar():
    """Detiene los dos motores."""
    wk.set_motors(1, 0)
    wk.set_motors(2, 0)


def current_time():
    """Tiempo actual en segundos (float)."""
    return utime.ticks_ms() / 1000.0


###########################################
# ODOMETRÍA (estimación por tiempo)
###########################################

_last_odom_time  = current_time()
_last_lin_speed  = 0.0   # velocidad lineal actual (cm/s positivo)
_last_ang_speed  = 0.0   # velocidad angular actual (deg/s positivo con signo)

def update_odometry():
    """
    Integra posición y orientación estimadas a partir del tiempo transcurrido
    y las últimas velocidades aplicadas. Se llama repetidamente en los bucles.
    """
    global x, y, theta, _last_odom_time

    now = current_time()
    dt  = now - _last_odom_time
    _last_odom_time = now

    # Avance lineal
    ds = _last_lin_speed * dt
    x     += ds * math.cos(theta)
    y     += ds * math.sin(theta)
    # Cambio angular
    theta += math.radians(_last_ang_speed * dt)


def _set_motor_and_track(linear_cm_s, angular_deg_s):
    """
    Llama a set_motor_speeds escalando al rango de motores (0-100)
    y registra las velocidades para la odometría.
    """
    global _last_lin_speed, _last_ang_speed
    _last_lin_speed  = linear_cm_s
    _last_ang_speed  = angular_deg_s

    # Escalamos: LINEAR_SPEED_CM_S → LINEAR_SPEED (100% motor)
    lin_m = (linear_cm_s  / LINEAR_SPEED_CM_S) * LINEAR_SPEED
    ang_m = (angular_deg_s / ANG_SPEED_DEG_S)  * ANGULAR_SPEED
    set_motor_speeds(lin_m, ang_m)


###########################################
# FUNCIONES GEOMÉTRICAS
###########################################

def dist_2d(a_x, a_y, b_x, b_y):
    """Distancia euclidiana entre dos puntos 2D."""
    dx = a_x - b_x
    dy = a_y - b_y
    return math.sqrt(dx*dx + dy*dy)


def angle_to_point(from_x, from_y, from_theta, to_x, to_y):
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
    return error


def project_point_on_main_trace(px, py):
    """
    Proyecta (px, py) sobre el segmento start → goal.
    Devuelve (tx, ty), el punto más cercano de la traza.
    """
    vx = goal_x - start_x
    vy = goal_y - start_y
    wx = px - start_x
    wy = py - start_y
    c2 = vx*vx + vy*vy
    if c2 == 0:
        return start_x, start_y
    t = (vx*wx + vy*wy) / c2
    t = max(0.0, min(1.0, t))
    return start_x + t*vx, start_y + t*vy


###########################################
# CONTROL DE NAVEGACIÓN
###########################################

ANG_TOL = 0.08   # rad — tolerancia angular para considerar "orientado"

def follow_point(target_x, target_y):
    """
    Avanza hacia (target_x, target_y).
    Primero gira hacia el punto y luego avanza en línea recta.
    Devuelve True cuando llega (dentro de WAYPOINT_TOLERANCE).
    """
    global x, y, theta

    ang_error = angle_to_point(x, y, theta, target_x, target_y)

    if abs(ang_error) > ANG_TOL:
        # Girar hacia el punto
        if ang_error > 0:
            _set_motor_and_track(0.0,  ANG_SPEED_DEG_S)
        else:
            _set_motor_and_track(0.0, -ANG_SPEED_DEG_S)
        return False
    else:
        # Avanzar
        _set_motor_and_track(LINEAR_SPEED_CM_S, 0.0)

    d = dist_2d(x, y, target_x, target_y)
    if d < WAYPOINT_TOLERANCE:
        Parar()
        return True
    return False


def follow_point_until_reach(tx, ty):
    """
    Bucle que llama a follow_point hasta llegar a (tx, ty).
    Se detiene también si se pulsa el botón de emergencia (button_b).
    """
    while not button_b.is_pressed():
        update_odometry()
        if follow_point(tx, ty):
            break


###########################################
# GIROS Y RECTAS CRONOMETRADOS
###########################################

def turn_angle(angle_degrees):
    """
    Gira el robot exactamente 'angle_degrees' grados usando tiempo.
    Positivo = izquierda, Negativo = derecha.
    Actualiza theta.
    """
    global theta

    if angle_degrees == 0:
        return

    direction = 1 if angle_degrees > 0 else -1
    _set_motor_and_track(0.0, direction * ANG_SPEED_DEG_S)

    t_needed = abs(angle_degrees) / ANG_SPEED_DEG_S   # segundos
    t_start  = current_time()
    while current_time() - t_start < t_needed:
        update_odometry()
        if button_b.is_pressed():
            break

    Parar()
    theta += math.radians(angle_degrees)
    # Normalizar theta a [-pi, pi]
    while theta >  math.pi: theta -= 2.0 * math.pi
    while theta < -math.pi: theta += 2.0 * math.pi

    _last_lin_speed_reset()


def move_straight(distance_cm):
    """
    Avanza en línea recta 'distance_cm' centímetros usando tiempo.
    """
    _set_motor_and_track(LINEAR_SPEED_CM_S, 0.0)

    t_needed = distance_cm / LINEAR_SPEED_CM_S   # segundos
    t_start  = current_time()
    while current_time() - t_start < t_needed:
        update_odometry()
        if button_b.is_pressed():
            break

    Parar()
    _last_lin_speed_reset()


def _last_lin_speed_reset():
    """Resetea la velocidad interna tras una parada."""
    global _last_lin_speed, _last_ang_speed
    _last_lin_speed = 0.0
    _last_ang_speed = 0.0


def turn_to_orientation(target_theta):
    """
    Gira hasta alcanzar una orientación absoluta target_theta (radianes).
    """
    global theta

    while not button_b.is_pressed():
        update_odometry()
        error = target_theta - theta
        # Normalizar a [-pi, pi]
        while error >  math.pi: error -= 2.0 * math.pi
        while error < -math.pi: error += 2.0 * math.pi

        if abs(error) < 0.05:
            Parar()
            _last_lin_speed_reset()
            break
        else:
            if error > 0:
                _set_motor_and_track(0.0,  ANG_SPEED_DEG_S)
            else:
                _set_motor_and_track(0.0, -ANG_SPEED_DEG_S)


###########################################
# MANIOBRA DE ESQUIVA
###########################################

def avoid_obstacle_maneuver():
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
    global stored_trace_point, stored_trace_theta

    # 1) Guardar punto y orientación de la traza
    stored_trace_point = project_point_on_main_trace(x, y)
    stored_trace_theta = theta

    # Distancias de maniobra — ajusta según el tamaño real del robot y el obstáculo
    lateral_distance = 30.0   # cm de apartado lateral
    forward_distance = 50.0   # cm de avance para sobrepasar

    side_sign = +1 if avoid_side == "LEFT" else -1

    # 2) Girar 90° hacia el lado de esquiva
    turn_angle(90.0 * side_sign)

    # 3) Avanzar lateralmente
    move_straight(lateral_distance)

    # 4) Girar 90° de vuelta a la dirección de avance original
    turn_angle(-90.0 * side_sign)

    # 5) Avanzar para pasar el obstáculo
    move_straight(forward_distance)

    # 6) Girar 90° hacia la traza (hacia el interior)
    turn_angle(-90.0 * side_sign)

    # 7) Avanzar hasta la proyección de la traza
    target_x, target_y = stored_trace_point
    follow_point_until_reach(target_x, target_y)

    # 8) Recuperar orientación original
    turn_to_orientation(stored_trace_theta)


###########################################
# BUCLE PRINCIPAL
###########################################

display.show(Image.ARROW_N)   # indicador visual: robot listo

# Espera a que se pulse button_a para arrancar
while not button_a.is_pressed():
    sleep(100)

display.show(Image.YES)
_last_odom_time = current_time()   # reiniciar odometría desde cero

while True:
    # Botón de emergencia: para todo
    if button_b.is_pressed():
        Parar()
        display.show(Image.NO)
        break

    update_odometry()
    distance_obst = read_ultrasonic()

    if state == "GO_TO_GOAL":
        if 0 < distance_obst < ULTRASONIC_THRESHOLD:
            # Obstáculo detectado → cambiar a modo esquiva
            Parar()
            display.show(Image.SAD)
            state = "AVOID_OBSTACLE"
        else:
            reached_goal = follow_point(goal_x, goal_y)
            if reached_goal:
                Parar()
                display.show(Image.HAPPY)
                break   # Objetivo alcanzado — fin del programa

    elif state == "AVOID_OBSTACLE":
        avoid_obstacle_maneuver()
        # Tras la maniobra volvemos a navegar hacia el objetivo
        state = "GO_TO_GOAL"
        display.show(Image.ARROW_N)
