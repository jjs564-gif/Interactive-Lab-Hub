import sys
import termios
import tty
import time
import pi_servo_hat

# WasteWise Wizard-of-Oz prototype
# Space toggles between thumbs-up and thumbs-down.
# The distance sensor input is simulated by the operator.

SERVO_CHANNEL = 0

# Start conservatively. Increase DOWN_ANGLE only after testing.
UP_ANGLE = 60
DOWN_ANGLE = 150
STEP = 2
DELAY = 0.03

servo = pi_servo_hat.PiServoHat()
servo.restart()


def move_smoothly(start, end):
    direction = STEP if end > start else -STEP

    for angle in range(start, end, direction):
        servo.move_servo_position(SERVO_CHANNEL, angle)
        time.sleep(DELAY)

    servo.move_servo_position(SERVO_CHANNEL, end)


def get_key():
    """Read one keypress without requiring Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


current_angle = UP_ANGLE
servo.move_servo_position(SERVO_CHANNEL, current_angle)

print("\nWasteWise Demo")
print("SPACE: Toggle thumbs up/down")
print("q: Quit")
print("Distance sensing is simulated for this prototype.\n")

try:
    while True:
        key = get_key()

        if key.lower() == "q":
            break

        if key == " ":
            target = (
                DOWN_ANGLE
                if current_angle == UP_ANGLE
                else UP_ANGLE
            )

            move_smoothly(current_angle, target)
            current_angle = target

            print(
                f"\rServo position: {current_angle} degrees",
                flush=True
            )

except KeyboardInterrupt:
    pass

finally:
    print("\nDemo stopped.")
