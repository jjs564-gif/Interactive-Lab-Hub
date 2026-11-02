# Daybreak: Storyboard Feedback and Revisions

## Original Concept

Daybreak is a Raspberry Pi system that observes a window overnight, detects the arrival of daylight, and provides a quiet report when the user wakes up.

## Feedback Received

The concept was described as simple, repeatable, and privacy-conscious because the camera points toward the sky rather than toward the user.

The feedback also identified several concerns:
- Automatic webcam exposure could interfere with brightness measurements.
- The system should clearly define what counts as sunrise.
- Testing across multiple mornings would help evaluate reliability.
- A saved daylight photograph could make the morning report more meaningful.

## Revisions

I revised the system to detect the first sustained increase in daylight rather than claim to measure the exact astronomical sunrise.

I also added a requirement for several consecutive bright observations to reduce false detections caused by temporary changes in lighting.

The morning report will include the detected time, a representative photograph, and a short interpretation of the observations.

## Future Improvements

I would test the system over several mornings and compare its results under different weather conditions. I would also investigate the effects of automatic exposure and potentially calibrate the brightness threshold for the specific window.

## Design Rationale

These revisions preserve the original simplicity of Daybreak while making its sensing behavior more transparent, testable, and reliable.
