###########################################
# CONFIGURACIÓN INICIAL
###########################################

# Pose del robot (se actualiza con odometría o similar)
x, y = 0.0, 0.0          # posición inicial del robot
theta = 0.0              # orientación inicial del robot (rad)

# Objetivo global
goal_x, goal_y = 100.0, 0.0   # ejemplo: punto objetivo en el mapa

# Parámetros de control
LINEAR_SPEED = 0.2            # m/s
ANGULAR_SPEED = 0.5           # rad/s
ULTRASONIC_THRESHOLD = 0.25   # m, distancia mínima para considerar obstáculo
WAYPOINT_TOLERANCE = 0.05     # m, tolerancia para considerar que se llegó

# Estado principal del robot
state = "GO_TO_GOAL"          # otros: "AVOID_OBSTACLE", "RETURN_TO_TRACE"

# Variables para esquiva
stored_trace_point = None     # (x, y) punto de la traza donde se detectó el obstáculo
stored_trace_theta = None     # orientación en la traza al detectar el obstáculo
avoid_side = "LEFT"           # por defecto, esquiva a la izquierda


###########################################
# FUNCIONES BÁSICAS DE CONTROL
###########################################

def read_ultrasonic():
    """
    Lee la distancia medida por el ultrasonidos.
    Debes implementar esta función con tu hardware real.
    """ 
    distance = 999.0  # valor ficticio
    return distance

def set_motor_speeds(linear_vel, angular_vel):
    """
    Envía velocidades a los motores.
    Implementar según tu plataforma (PWM, librerías, etc.).
    """
    pass

def update_odometry():
    """
    Actualiza x, y, theta con odometría o sensores.
    Implementar según tu robot.
    """
    global x, y, theta
    # Actualización ficticia
    pass

def distance(a_x, a_y, b_x, b_y):
    dx = a_x - b_x
    dy = a_y - b_y
    return (dx**2 + dy**2) ** 0.5

def angle_to_point(from_x, from_y, from_theta, to_x, to_y):
    """
    Devuelve el ángulo que hay que girar (error de orientación)
    para mirar desde (from_x, from_y, from_theta) hacia (to_x, to_y).
    """
    import math
    dx = to_x - from_x
    dy = to_y - from_y
    desired_theta = math.atan2(dy, dx)
    error = desired_theta - from_theta
    # Normalizar a [-pi, pi]
    while error > math.pi:
        error -= 2 * math.pi
    while error < -math.pi:
        error += 2 * math.pi
    return error

def follow_point(target_x, target_y):
    """
    Control sencillo: gira hacia el punto y avanza.
    Devuelve True si hemos llegado al punto.
    """
    global x, y, theta

    # 1) Calcular error angular para orientar hacia el punto
    ang_error = angle_to_point(x, y, theta, target_x, target_y)

    # 2) Si el error angular es grande, girar casi sin avanzar
    ANG_TOL = 0.05  # tolerancia angular
    if abs(ang_error) > ANG_TOL:
        # girar en el sentido correcto
        if ang_error > 0:
            set_motor_speeds(0.0, ANGULAR_SPEED)
        else:
            set_motor_speeds(0.0, -ANGULAR_SPEED)
        return False
    else:
        # Orientado: avanzar hacia el punto
        set_motor_speeds(LINEAR_SPEED, 0.0)

    # 3) Comprobar distancia al punto
    d = distance(x, y, target_x, target_y)
    if d < WAYPOINT_TOLERANCE:
        # Hemos llegado al punto
        set_motor_speeds(0.0, 0.0)
        return True
    else:
        return False


###########################################
# CÁLCULO DE LA TRAZA PRINCIPAL
###########################################

# La traza principal es el segmento entre (start_x, start_y) y (goal_x, goal_y)
start_x, start_y = x, y

def project_point_on_main_trace(px, py):
    """
    Proyecta el punto (px, py) sobre el segmento de la traza principal
    entre (start_x, start_y) y (goal_x, goal_y). Devuelve (tx, ty).
    Útil si quieres recalcular un punto exacto de la traza.
    """
    import math
    vx = goal_x - start_x
    vy = goal_y - start_y
    wx = px - start_x
    wy = py - start_y

    # proyección escalar t en [0,1] sobre el segmento
    c1 = vx*wx + vy*wy
    c2 = vx*vx + vy*vy
    if c2 == 0:
        return start_x, start_y
    t = c1 / c2

    if t < 0:
        t = 0
    if t > 1:
        t = 1

    tx = start_x + t * vx
    ty = start_y + t * vy
    return tx, ty


###########################################
# MANIOBRA DE ESQUIVA (GIROS EXACTOS)
###########################################

def avoid_obstacle_maneuver():
    """
    Maniobra de esquivar:
    1) Guardamos el punto de la traza y la orientación.
    2) Giramos 90 grados hacia un lado (p.ej. izquierda).
    3) Avanzamos una distancia fija lateral para rodear.
    4) Giramos 90 grados en sentido contrario para volver a dirección original.
    5) Avanzamos una distancia suficiente para sobrepasar el obstáculo.
    6) Giramos 90 grados hacia el lado contrario para volver a la traza.
    7) Avanzamos hacia el punto proyectado en la traza.
    8) Giramos 90 grados final para recuperar la orientación almacenada.
    """

    global x, y, theta, stored_trace_point, stored_trace_theta

    # 1) Guardar punto y orientación actuales de la traza
    stored_trace_point = project_point_on_main_trace(x, y)
    stored_trace_theta = theta

    # Distancias para la maniobra (ajusta según tamaño del robot y obstáculo)
    lateral_distance = 0.30      # metros que nos apartamos lateralmente
    forward_distance = 0.50      # metros para pasar el obstáculo

    # 2) Girar 90 grados hacia el lado de esquiva
    # Supondremos que la función turn_angle(angle_rad) gira el robot
    if avoid_side == "LEFT":
        turn_angle(+90.0)   # grados
    else:
        turn_angle(-90.0)

    # 3) Avanzar lateralmente
    move_straight(lateral_distance)

    # 4) Girar 90 grados hacia el sentido original de avance
    if avoid_side == "LEFT":
        turn_angle(-90.0)
    else:
        turn_angle(+90.0)

    # 5) Avanzar hacia delante para sobrepasar el obstáculo
    move_straight(forward_distance)

    # 6) Girar 90 grados en el lado contrario para volver hacia la traza
    if avoid_side == "LEFT":
        turn_angle(-90.0)
    else:
        turn_angle(+90.0)

    # 7) Avanzar lateralmente hacia la traza hasta la proyección guardada
    target_x, target_y = stored_trace_point
    follow_point_until_reach(target_x, target_y)

    # 8) Girar para recuperar la orientación original de la traza
    turn_to_orientation(stored_trace_theta)


def turn_angle(angle_degrees):
    """
    Gira el robot un ángulo fijo en grados.
    Ejemplo exacto para 90 grados:

    - Para +90 grados (giro a la izquierda):
        1) Fijar velocidad angular positiva (ANGULAR_SPEED).
        2) Calcular tiempo_t = 90° / (vel_angular_en_deg_por_seg).
        3) Mantener giro ese tiempo_t y luego parar.

    Debes calibrar vel_angular_en_deg_por_seg para tu robot real.
    """
    import time
    global theta

    # Conversión aproximada de rad/s a deg/s
    deg_per_sec = ANGULAR_SPEED * 180.0 / 3.14159

    # Definimos sentido de giro
    if angle_degrees > 0:
        set_motor_speeds(0.0, ANGULAR_SPEED)  # giro izquierda
    else:
        set_motor_speeds(0.0, -ANGULAR_SPEED) # giro derecha

    t = abs(angle_degrees) / deg_per_sec
    start_time = current_time()
    while current_time() - start_time < t:
        update_odometry()

    set_motor_speeds(0.0, 0.0)

    # Actualizar orientación aproximada
    theta += angle_degrees * 3.14159 / 180.0


def move_straight(distance_m):
    """
    Avanza en línea recta una distancia concreta.
    """
    import time
    global x, y, theta

    speed = LINEAR_SPEED  # m/s
    t = distance_m / speed

    set_motor_speeds(speed, 0.0)
    start_time = current_time()
    while current_time() - start_time < t:
        update_odometry()

    set_motor_speeds(0.0, 0.0)


def follow_point_until_reach(tx, ty):
    """
    Igual que follow_point, pero en un bucle interno
    hasta llegar al punto.
    """
    reached = False
    while not reached:
        update_odometry()
        distance_obst = read_ultrasonic()
        # OJO: aquí puedes decidir ignorar el ultrasonidos
        # mientras estás volviendo a la traza, o volver a esquivar de nuevo.
        reached = follow_point(tx, ty)


def turn_to_orientation(target_theta):
    """
    Gira el robot hasta una orientación absoluta target_theta.
    """
    global theta
    import math

    done = False
    while not done:
        update_odometry()
        error = target_theta - theta
        # Normalizar a [-pi, pi]
        while error > math.pi:
            error -= 2 * math.pi
        while error < -math.pi:
            error += 2 * math.pi

        if abs(error) < 0.05:
            set_motor_speeds(0.0, 0.0)
            done = True
        else:
            if error > 0:
                set_motor_speeds(0.0, ANGULAR_SPEED)
            else:
                set_motor_speeds(0.0, -ANGULAR_SPEED)


def current_time():
    """
    Devuelve el tiempo actual en segundos.
    Implementa con time.time() o temporizador de tu placa.
    """
    import time
    return time.time()


###########################################
# BUCLE PRINCIPAL
###########################################

while True:
    update_odometry()
    distance_obst = read_ultrasonic()

    if state == "GO_TO_GOAL":
        # Control normal hacia objetivo global
        if distance_obst < ULTRASONIC_THRESHOLD:
            # Objeto detectado, cambiar a esquiva
            state = "AVOID_OBSTACLE"
        else:
            reached_goal = follow_point(goal_x, goal_y)
            if reached_goal:
                set_motor_speeds(0.0, 0.0)
                break  # Objetivo alcanzado

    elif state == "AVOID_OBSTACLE":
        # Ejecutar maniobra completa de esquiva
        avoid_obstacle_maneuver()
        # Al terminar, volvemos a la traza original
        state = "GO_TO_GOAL"

    # Pequeño retardo de bucle si hace falta
    # time.sleep(0.01)
