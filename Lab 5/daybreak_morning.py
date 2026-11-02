
#!/usr/bin/env python3
"""Daybreak morning report from overnight camera brightness observations."""

import argparse
import json
from datetime import datetime
from pathlib import Path

DEFAULT_DATA = Path("daybreak_data")


def format_time(timestamp):
    if not timestamp:
        return "unknown time"
    try:
        return datetime.fromisoformat(timestamp).strftime("%I:%M:%S %p").lstrip("0")
    except ValueError:
        return str(timestamp)


def load_json(path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def count_samples(path):
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def main():
    parser = argparse.ArgumentParser(description="Daybreak morning reveal")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--speak", action="store_true")
    args = parser.parse_args()

    event_path = args.data / "logs" / "daybreak_event.json"
    log_path = args.data / "logs" / "daybreak_log.jsonl"

    event = load_json(event_path)
    samples = count_samples(log_path)

    if event:
        detected = format_time(event.get("detected_at"))
        confirmed = format_time(event.get("confirmed_at"))
        message = (
            f"Good morning. Daybreak first detected sustained brightness "
            f"at {detected}, confirmed at {confirmed}. "
            f"The observation contains {samples} recorded samples."
        )
        photo = event.get("photo")
    else:
        message = (
            f"Good morning. Daybreak recorded {samples} samples, "
            "but no sustained daylight event was confirmed."
        )
        photo = None

    print("\n" + "=" * 48)
    print("DAYBREAK | MORNING REVEAL")
    print("=" * 48)
    print(message)
    if photo:
        print(f"Captured image: {photo}")
    print("=" * 48 + "\n")

    if args.speak:
        import shutil
        import subprocess

        if shutil.which("espeak-ng"):
            subprocess.run(["espeak-ng", message], check=False)
        elif shutil.which("espeak"):
            subprocess.run(["espeak", message], check=False)
        else:
            print("Speech unavailable: install espeak-ng or use Piper.")


if __name__ == "__main__":
    main()
