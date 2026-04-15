import board
import busio
import time
import random
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# =========================
# USER SPEED CONTROL
# =========================
SPEED = 3

# =========================
# I2C + PCA9685
# =========================
i2c = busio.I2C(board.GP1, board.GP0)
pca = PCA9685(i2c)
pca.frequency = 50

# =========================
# Servo mapping
# =========================
back_right_leg   = servo.Servo(pca.channels[0])
back_right_foot  = servo.Servo(pca.channels[1])

back_left_leg    = servo.Servo(pca.channels[2])
back_left_foot   = servo.Servo(pca.channels[4])

front_left_leg   = servo.Servo(pca.channels[12])
front_right_foot = servo.Servo(pca.channels[13])
front_right_leg  = servo.Servo(pca.channels[14])
front_left_foot  = servo.Servo(pca.channels[15])

# =========================
# Base standing pose
# =========================
BL_LEG_BASE = 150
BL_FOOT_BASE = 80

BR_LEG_BASE = 30
BR_FOOT_BASE = 100

FL_LEG_BASE = 90
FL_FOOT_BASE = 60

FR_LEG_BASE = 120
FR_FOOT_BASE = 130

# =========================
# Gait tuning
# =========================
LEG_SWING = 20
FOOT_LIFT = 20
STEP_DELAY = 0.01
BODY_PUSH = 10

# Turning tuning
TURN_INNER_SCALE = 0.45
TURN_OUTER_SCALE = 1.00

# Forward correction
FORWARD_TRIM = 6

# Stronger right turn
RIGHT_TURN_BOOST = 10

# Random zig-zag tuning
ZIGZAG_FORWARD_MIN = 3
ZIGZAG_FORWARD_MAX = 7
ZIGZAG_TURN_MIN = 1
ZIGZAG_TURN_MAX = 6
ZIGZAG_PAUSE = 0.15

# =========================
# Helpers
# =========================
def clamp_angle(a):
    if a < 0:
        return 0
    if a > 180:
        return 180
    return int(a)

def move_servo_slow(servo_obj, start, end, step=1, delay=0.01):
    delay = delay / SPEED
    step = max(1, int(step * SPEED))

    start = clamp_angle(start)
    end = clamp_angle(end)

    if start < end:
        for a in range(start, end + 1, step):
            servo_obj.angle = a
            time.sleep(delay)
        servo_obj.angle = end
    else:
        for a in range(start, end - 1, -step):
            servo_obj.angle = a
            time.sleep(delay)
        servo_obj.angle = end

def stand():
    back_left_leg.angle = BL_LEG_BASE
    back_left_foot.angle = BL_FOOT_BASE

    back_right_leg.angle = BR_LEG_BASE
    back_right_foot.angle = BR_FOOT_BASE

    front_left_leg.angle = FL_LEG_BASE
    front_left_foot.angle = FL_FOOT_BASE

    front_right_leg.angle = FR_LEG_BASE
    front_right_foot.angle = FR_FOOT_BASE

def sit():
    back_left_foot.angle = 0
    back_right_foot.angle = 180
    front_right_foot.angle = 180
    front_left_foot.angle = 0

def def_stop():
    stand()

# =========================
# Diagonal pair 1
# front_left + back_right
# =========================
def move_pair(fl_leg_target, fl_foot_target,
              br_leg_target, br_foot_target,
              fr_leg_target, bl_leg_target):

    # Lift moving pair
    move_servo_slow(front_left_foot, FL_FOOT_BASE, fl_foot_target, delay=STEP_DELAY)
    move_servo_slow(back_right_foot, BR_FOOT_BASE, br_foot_target, delay=STEP_DELAY)

    # Swing moving pair forward
    move_servo_slow(front_left_leg, FL_LEG_BASE, fl_leg_target, delay=STEP_DELAY)
    move_servo_slow(back_right_leg, BR_LEG_BASE, br_leg_target, delay=STEP_DELAY)

    # Supporting pair push body
    move_servo_slow(front_right_leg, FR_LEG_BASE, fr_leg_target, delay=STEP_DELAY)
    move_servo_slow(back_left_leg, BL_LEG_BASE, bl_leg_target, delay=STEP_DELAY)

    # Put moving pair down
    move_servo_slow(front_left_foot, fl_foot_target, FL_FOOT_BASE, delay=STEP_DELAY)
    move_servo_slow(back_right_foot, br_foot_target, BR_FOOT_BASE, delay=STEP_DELAY)

    time.sleep(0.03 / SPEED)

    # Return all legs to base
    move_servo_slow(front_left_leg, fl_leg_target, FL_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(back_right_leg, br_leg_target, BR_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(front_right_leg, fr_leg_target, FR_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(back_left_leg, bl_leg_target, BL_LEG_BASE, delay=STEP_DELAY)

# =========================
# Diagonal pair 2
# front_right + back_left
# =========================
def move_pair_2(fr_leg_target, fr_foot_target,
                bl_leg_target, bl_foot_target,
                fl_leg_target, br_leg_target):

    # Lift moving pair
    move_servo_slow(front_right_foot, FR_FOOT_BASE, fr_foot_target, delay=STEP_DELAY)
    move_servo_slow(back_left_foot, BL_FOOT_BASE, bl_foot_target, delay=STEP_DELAY)

    # Swing moving pair forward
    move_servo_slow(front_right_leg, FR_LEG_BASE, fr_leg_target, delay=STEP_DELAY)
    move_servo_slow(back_left_leg, BL_LEG_BASE, bl_leg_target, delay=STEP_DELAY)

    # Supporting pair push body
    move_servo_slow(front_left_leg, FL_LEG_BASE, fl_leg_target, delay=STEP_DELAY)
    move_servo_slow(back_right_leg, BR_LEG_BASE, br_leg_target, delay=STEP_DELAY)

    # Put moving pair down
    move_servo_slow(front_right_foot, fr_foot_target, FR_FOOT_BASE, delay=STEP_DELAY)
    move_servo_slow(back_left_foot, bl_foot_target, BL_FOOT_BASE, delay=STEP_DELAY)

    time.sleep(0.03 / SPEED)

    # Return all legs to base
    move_servo_slow(front_right_leg, fr_leg_target, FR_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(back_left_leg, bl_leg_target, BL_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(front_left_leg, fl_leg_target, FL_LEG_BASE, delay=STEP_DELAY)
    move_servo_slow(back_right_leg, br_leg_target, BR_LEG_BASE, delay=STEP_DELAY)

# =========================
# Forward gait
# =========================
def walk_forward():
    move_pair(
        fl_leg_target=FL_LEG_BASE - LEG_SWING,
        fl_foot_target=FL_FOOT_BASE - FOOT_LIFT,
        br_leg_target=BR_LEG_BASE + LEG_SWING + FORWARD_TRIM,
        br_foot_target=BR_FOOT_BASE + FOOT_LIFT,
        fr_leg_target=FR_LEG_BASE - BODY_PUSH - FORWARD_TRIM,
        bl_leg_target=BL_LEG_BASE + BODY_PUSH
    )

    move_pair_2(
        fr_leg_target=FR_LEG_BASE + LEG_SWING + FORWARD_TRIM,
        fr_foot_target=FR_FOOT_BASE + FOOT_LIFT,
        bl_leg_target=BL_LEG_BASE - LEG_SWING,
        bl_foot_target=BL_FOOT_BASE - FOOT_LIFT,
        fl_leg_target=FL_LEG_BASE + BODY_PUSH,
        br_leg_target=BR_LEG_BASE - BODY_PUSH - FORWARD_TRIM
    )

# =========================
# Left turn gait
# =========================
def walk_left():
    move_pair(
        fl_leg_target=FL_LEG_BASE - int(LEG_SWING * TURN_INNER_SCALE),
        fl_foot_target=FL_FOOT_BASE - FOOT_LIFT,
        br_leg_target=BR_LEG_BASE + int(LEG_SWING * TURN_OUTER_SCALE),
        br_foot_target=BR_FOOT_BASE + FOOT_LIFT,
        fr_leg_target=FR_LEG_BASE - BODY_PUSH,
        bl_leg_target=BL_LEG_BASE + int(BODY_PUSH * TURN_INNER_SCALE)
    )

    move_pair_2(
        fr_leg_target=FR_LEG_BASE + int(LEG_SWING * TURN_OUTER_SCALE),
        fr_foot_target=FR_FOOT_BASE + FOOT_LIFT,
        bl_leg_target=BL_LEG_BASE - int(LEG_SWING * TURN_INNER_SCALE),
        bl_foot_target=BL_FOOT_BASE - FOOT_LIFT,
        fl_leg_target=FL_LEG_BASE + int(BODY_PUSH * TURN_INNER_SCALE),
        br_leg_target=BR_LEG_BASE - BODY_PUSH
    )

# =========================
# Right turn gait
# =========================
def walk_right():
    move_pair(
        fl_leg_target=FL_LEG_BASE - (LEG_SWING + RIGHT_TURN_BOOST),
        fl_foot_target=FL_FOOT_BASE - FOOT_LIFT,
        br_leg_target=BR_LEG_BASE + int(LEG_SWING * 0.35),
        br_foot_target=BR_FOOT_BASE + FOOT_LIFT,
        fr_leg_target=FR_LEG_BASE - int(BODY_PUSH * 0.35),
        bl_leg_target=BL_LEG_BASE + BODY_PUSH + RIGHT_TURN_BOOST
    )

    move_pair_2(
        fr_leg_target=FR_LEG_BASE + int(LEG_SWING * 0.35),
        fr_foot_target=FR_FOOT_BASE + FOOT_LIFT,
        bl_leg_target=BL_LEG_BASE - (LEG_SWING + RIGHT_TURN_BOOST),
        bl_foot_target=BL_FOOT_BASE - FOOT_LIFT,
        fl_leg_target=FL_LEG_BASE + BODY_PUSH + RIGHT_TURN_BOOST,
        br_leg_target=BR_LEG_BASE - int(BODY_PUSH * 0.35)
    )

# =========================
# 360 turns
# =========================
def turn_left_360():
    for _ in range(20):
        walk_left()

def turn_right_360():
    for _ in range(20):
        walk_right()

# =========================
# Random zig-zag
# =========================
def random_zigzag():
    # Forward burst
    forward_steps = random.randint(ZIGZAG_FORWARD_MIN, ZIGZAG_FORWARD_MAX)
    for _ in range(forward_steps):
        walk_forward()

    time.sleep(ZIGZAG_PAUSE)

    # Turn left
    left_steps = random.randint(ZIGZAG_TURN_MIN, ZIGZAG_TURN_MAX)
    for _ in range(left_steps):
        walk_left()

    time.sleep(ZIGZAG_PAUSE)

    # Forward burst
    forward_steps = random.randint(ZIGZAG_FORWARD_MIN, ZIGZAG_FORWARD_MAX)
    for _ in range(forward_steps):
        walk_forward()

    time.sleep(ZIGZAG_PAUSE)

    # Turn right
    right_steps = random.randint(ZIGZAG_TURN_MIN, ZIGZAG_TURN_MAX)
    for _ in range(right_steps):
        walk_right()

    time.sleep(ZIGZAG_PAUSE)

# =========================
# Main
# =========================
try:
    sit()
    time.sleep(1.5)

    stand()
    time.sleep(2)

    while True:
        random_zigzag()
        # walk_forward()
        # walk_left()
        # walk_right()
        # turn_left_360()
        # turn_right_360()

except KeyboardInterrupt:
    stand()
    time.sleep(1)
    pca.deinit()