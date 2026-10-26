# Lab 5 Part E: YOLO to Qwen Integration

## Experimental Setup

I connected a USB webcam to the Raspberry Pi and ran the YOLO-to-Qwen pipeline in headless mode over SSH.

During the observation period, I remained in the camera's field of view and performed several hand and body movements.

## Results

- Observation duration: approximately 60 seconds
- Logged observations: 6
- YOLO detections: mostly one person at center/close or right/close
- Maximum simultaneous detections: 2 people in one observation
- Qwen reasoning time: 8.8 seconds

## Interpretation

The system successfully detected a person, interpreted changes in position, recorded observations, and passed the resulting log to Qwen.

However, Qwen incorrectly concluded that three people were present and that one remained stationary throughout the entire observation period.

This illustrates a limitation of language-model reasoning: a generated summary may introduce claims that are not supported by the underlying sensor data.

The hand movements were not independently recognized because the interpreter was configured to track person count, position, and apparent distance rather than hand landmarks.

## Design Takeaway

For a reliable observant system, I would preserve the original observation log, distinguish uncertain detections from confirmed events, and constrain the reasoning model to summarize only what the sensor data supports.
