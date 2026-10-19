import time
import qwiic_proximity
import pi_servo_hat

# WasteWise: Automatic sensing and physical feedback
# VCNL4040 proximity sensor -> Servo-driven cardboard thumb

# Servo configuration
SERVO_CHANNEL = 0
UP_ANGLE = 60
DOWN_ANGLE = 150
STEP = 2
DELAY = 0.03

# Initial thresholds (adjust after testing with a plate)
DETECT_THRESHOLD = 200
CLEAR_THRESHOLD = 180
POLL_INTERVAL = 0.2

# Initialize the proximity sensor
sensor = qwiic_proximity.QwiicProximity()

if not sensor.connected:
    raise RuntimeError("VCNL4040 not detected. Check Qwiic connection.")

sensor.begin()

# Initialize the servo
servo = pi_servo_hat.PiServoHat()
servo.restart()


def move_smoothly(start, end):
    """Move the servo gradually between two angles."""
    direction = STEP if end > start else -STEP

    for angle in range(start, end, direction):
        servo.move_servo_position(SERVO_CHANNEL, angle)
        time.sleep(DELAY)

    servo.move_servo_position(SERVO_CHANNEL, end)


# Start in thumbs-up position
current_angle = UP_ANGLE
servo.move_servo_position(SERVO_CHANNEL, current_angle)

# Track the detection state to avoid repeated servo movement
object_detected = False

print("\nWasteWise: Automatic Sensor-Driven Prototype")
print("Move an object toward and away from the distance sensor.")
print(f"Detect threshold: {DETECT_THRESHOLD}")
print(f"Clear threshold: {CLEAR_THRESHOLD}")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        reading = sensor.get_proximity()

        # Object enters detection region
        if not object_detected and reading >= DETECT_THRESHOLD:
            print(f"Proximity: {reading} | Object detected -> THUMBS DOWN")
            move_smoothly(current_angle, DOWN_ANGLE)
            current_angle = DOWN_ANGLE
            object_detected = True

        # Object leaves detection region
        elif object_detected and reading <= CLEAR_THRESHOLD:
            print(f"Proximity: {reading} | Region clear -> THUMBS UP")
            move_smoothly(current_angle, UP_ANGLE)
            current_angle = UP_ANGLE
            object_detected = False

        else:
            print(
                f"\rProximity: {reading:5d} | "
                f"State: {'THUMBS DOWN' if object_detected else 'THUMBS UP'}",
                end="",
                flush=True
            )

        time.sleep(POLL_INTERVAL)

except KeyboardInterrupt:
    print("\nWasteWise stopped.")
