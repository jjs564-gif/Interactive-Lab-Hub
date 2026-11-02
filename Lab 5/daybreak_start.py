
#!/usr/bin/env python3
"""Daybreak bedtime handoff with spoken acknowledgment."""

import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Start Daybreak with a spoken good-night acknowledgment."
    )
    parser.add_argument("--interval", type=float, default=30)
    parser.add_argument("--threshold", type=float, default=8)
    parser.add_argument("--consecutive", type=int, default=3)
    parser.add_argument("--duration", type=float, default=None)
    args = parser.parse_args()

    if args.interval <= 0 or args.consecutive < 1:
        parser.error("Interval must be positive and consecutive must be at least 1.")

    detector = Path(__file__).resolve().parent / "daybreak_overnight.py"

    if not detector.exists():
        sys.exit("Error: daybreak_overnight.py was not found.")

    print("\nDAYBREAK | BEDTIME HANDOFF", flush=True)
    print("Camera: window-facing", flush=True)
    print("Beginning overnight observation.", flush=True)

    acknowledgment = (
        "Good night. Daybreak is ready. "
        "I'll watch for the first sustained daylight. "
        "Sleep well."
    )

    subprocess.run(
        ["espeak-ng", "-s", "135", "-a", "65", acknowledgment],
        check=False,
    )

    command = [
        sys.executable,
        str(detector),
        "--interval", str(args.interval),
        "--threshold", str(args.threshold),
        "--consecutive", str(args.consecutive),
    ]

    if args.duration is not None:
        command.extend(["--duration", str(args.duration)])

    print("Handoff complete. Daybreak is now observing.\n", flush=True)

    try:
        subprocess.run(command, check=True)
    except KeyboardInterrupt:
        print("\nDaybreak observation stopped.")
    except subprocess.CalledProcessError as error:
        sys.exit(f"Daybreak stopped with error code {error.returncode}.")


if __name__ == "__main__":
    main()
