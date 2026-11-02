
import argparse
import cv2
import datetime
import json
import pathlib
import time

DATA = pathlib.Path("daybreak_data")
LOGS = DATA / "logs"
PHOTOS = DATA / "photos"

LOGS.mkdir(parents=True, exist_ok=True)
PHOTOS.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser(description="Daybreak overnight observer")
parser.add_argument("--interval", type=float, default=15)
parser.add_argument("--threshold", type=float, default=25)
parser.add_argument("--consecutive", type=int, default=4)
parser.add_argument("--duration", type=float, default=0,
                    help="Optional duration in seconds; 0 runs until Ctrl-C")
args = parser.parse_args()

if args.interval <= 0 or args.consecutive < 1 or args.duration < 0:
    parser.error("Invalid interval, consecutive count, or duration")

log_path = LOGS / "daybreak_log.jsonl"
event_path = LOGS / "daybreak_event.json"

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    raise RuntimeError("Could not open webcam")

print("DAYBREAK | Night observation started")
print("Camera: window-facing")
print("Sampling interval:", args.interval, "seconds")
print("Press Ctrl-C to finish.", flush=True)

baseline_samples = []
baseline = None
streak = 0
candidate_time = None
candidate_frame = None
detected = False
start = time.monotonic()

try:
    with open(log_path, "w") as log:
        while True:
            if args.duration and time.monotonic() - start >= args.duration:
                break

            for _ in range(5):
                cap.read()

            ok, frame = cap.read()
            if not ok:
                print("Camera frame unavailable; retrying.", flush=True)
                time.sleep(args.interval)
                continue

            now = datetime.datetime.now().astimezone()
            timestamp = now.isoformat(timespec="seconds")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            brightness = float(gray.mean())

            if baseline is None:
                baseline_samples.append(brightness)
                if len(baseline_samples) >= 4:
                    baseline = sum(baseline_samples) / len(baseline_samples)
                    print(f"Night baseline established: {baseline:.2f}",
                          flush=True)

            above = (
                baseline is not None
                and brightness >= baseline + args.threshold
            )

            if not detected:
                if above:
                    if streak == 0:
                        candidate_time = timestamp
                        candidate_frame = frame.copy()
                    streak += 1
                else:
                    streak = 0
                    candidate_time = None
                    candidate_frame = None

                if streak >= args.consecutive:
                    detected = True
                    photo_path = PHOTOS / "first_sustained_daylight.jpg"
                    cv2.imwrite(str(photo_path), candidate_frame)

                    event = {
                        "detected_at": candidate_time,
                        "confirmed_at": timestamp,
                        "baseline": round(baseline, 2),
                        "threshold_increase": args.threshold,
                        "consecutive_samples": args.consecutive,
                        "photo": str(photo_path),
                    }

                    event_path.write_text(json.dumps(event, indent=2))
                    print("Sustained daylight detected:", candidate_time,
                          flush=True)

            entry = {
                "timestamp": timestamp,
                "brightness": round(brightness, 2),
                "baseline": round(baseline, 2) if baseline is not None else None,
                "above_threshold": above,
                "streak": streak,
                "daylight_detected": detected,
            }

            log.write(json.dumps(entry) + "\n")
            log.flush()

            print(
                f"{timestamp} | brightness={brightness:.1f} "
                f"| streak={streak} | detected={detected}",
                flush=True
            )

            time.sleep(args.interval)

except KeyboardInterrupt:
    print("\nDaybreak observation stopped.")

finally:
    cap.release()
    print("Camera released. Log saved to:", log_path)
