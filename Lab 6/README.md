# Lab 6: Distributed Interaction

**ECE 5413 | Developing and Designing Interactive Devices**  
**Fall 2026 | Cornell Tech**

**Project:** NEON RACE | A Distributed Multiplayer Reaction Game

**Team:** Three-person collaborative project. Final demonstration completed with two active Raspberry Pis following consultation with DTA Albert.

**Author:** Jonathan Sharpy (GitHub: `jjs564-gif`)

---

# Part A: MQTT Messaging

## A.1 Introduction

The first part of Lab 6 introduced MQTT (Message Queuing Telemetry Transport), a lightweight communication protocol commonly used in Internet of Things applications.

Unlike direct device-to-device communication, MQTT uses a publish/subscribe architecture. Devices publish messages to named topics, while other devices subscribe to those topics to receive updates. A central broker manages message delivery.

This architecture allows multiple Raspberry Pis to communicate without maintaining direct connections to one another.

## A.2 MQTT Setup and Testing

We installed the Mosquitto MQTT command-line clients on the Raspberry Pi and connected to the Cornell course broker.

Our test used the following configuration:

| Parameter | Value |
|---|---|
| Broker | `farlab.infosci.cornell.edu` |
| Port | `1883` |
| Test topic | `IDD/test/jjs564` |
| Communication model | Publish/subscribe |

We opened two SSH sessions connected to the Raspberry Pi. One acted as a subscriber, while the other published a test message.

**Subscriber command:**

```bash
mosquitto_sub \
  -h farlab.infosci.cornell.edu \
  -p 1883 \
  -t 'IDD/test/jjs564' \
  -u idd \
  -P 'device@theFarm' \
  -v
```

**Publisher command:**

```bash
mosquitto_pub \
  -h farlab.infosci.cornell.edu \
  -p 1883 \
  -t 'IDD/test/jjs564' \
  -m 'Hello from my Raspberry Pi! Lab 6 MQTT test successful.' \
  -u idd \
  -P 'device@theFarm'
```

The subscriber successfully received the message, confirming that our Raspberry Pi could publish and subscribe through the broker.

### Publisher Evidence

![Successful MQTT publisher](media/mqtt_tests/Lab6A_MQTT_Publisher_Sent.png)

### Subscriber Evidence

![Successful MQTT subscriber](media/mqtt_tests/Lab6A_MQTT_Subscriber_Received.png)

## A.3 Five Distributed Interaction Ideas

We considered five possible applications of MQTT communication:

| Concept | Distributed Interaction |
|---|---|
| Distributed Daybreak | Multiple Raspberry Pis monitor brightness at different windows and collectively identify the first location to receive daylight. |
| Collaborative Mood Lamp | Each Pi measures a color or brightness value, and the devices collectively determine the output of a shared light. |
| Smart Room Presence | Proximity sensors report occupancy to a shared display that visualizes activity across multiple rooms. |
| Distributed Fitness Coach | Multiple motion-sensing devices contribute measurements to a combined exercise-feedback system. |
| Cooperative Soundscape | Multiple participants control different musical parameters using physical sensors and MQTT messaging. |

These ideas illustrated how distributed systems can combine independent physical inputs into a shared experience.

The main design consideration was defining meaningful MQTT topics and message formats so that devices could interpret one another's events consistently.

---

# Part B: Collaborative Pixel Grid

## B.1 Objective

Part B explored distributed sensing through a collaborative pixel grid.

Each participating Raspberry Pi represented a pixel in a shared browser interface. An APDS-9960 sensor measured the color of nearby physical objects, and the Raspberry Pi published those measurements through MQTT.

The shared system converted individual sensor readings into a collective visual display.

## B.2 Hardware

Our Raspberry Pi setup included:

- Raspberry Pi with network connectivity
- Adafruit miniPiTFT display
- APDS-9960 RGB, proximity, and gesture sensor
- Qwiic connection
- External colored objects for testing

### Hardware Setup

![Raspberry Pi with APDS-9960 sensor](media/part_b_images/Lab6B_Raspberry_Pi_APDS9960_Setup.jpg)

The APDS-9960 provided physical color measurements. The Raspberry Pi processed those measurements and communicated with the shared pixel-grid system.

## B.3 System Architecture

```text
Physical Colored Object
          |
          v
    APDS-9960 Sensor
          |
       I2C / Qwiic
          |
          v
      Raspberry Pi
          |
    RGB Measurement
          |
          v
     MQTT Publisher
          |
          v
       MQTT Broker
          |
          v
   Shared Grid Server
          |
          v
       Web Browser
```

This architecture separated physical sensing, message transmission, and visual output.

## B.4 Implementation and Testing

We used the provided `pixel_grid_publisher.py` script to read sensor values and publish color information.

The shared grid could then visualize the colors detected by multiple devices.

For our physical test, we used the blue cap of a Spider-Man water bottle.

When the sensor faced the cap, the corresponding pixel in the shared grid changed to blue.

### Physical Color Test

![Blue cap presented to RGB sensor](media/part_b_images/Lab6B_RGB_Sensor_Blue_Cap_Test.jpg)

### Collaborative Pixel Grid

![Collaborative pixel grid](media/part_b_images/Lab6B_Collaborative_Pixel_Grid.png)

The top-right pixel displayed blue during our demonstration, matching the object placed near our sensor.

## B.5 Observations

This experiment demonstrated that physical sensor measurements could be transmitted through a network and reflected in a shared interface.

The interaction also showed why distributed systems require more than working individual sensors. The publisher, MQTT broker, receiving server, and browser interface must all communicate correctly.

The successful color response confirmed that our device could contribute meaningful input to a multi-device experience.

---

# Part C: NEON RACE | Distributed Multiplayer Reaction Game

## C.1 Project Overview

For Part C, our team developed **NEON RACE**, a multiplayer physical reaction game built around Raspberry Pis, sensor inputs, MQTT messaging, and small interactive displays.

The concept combines a traditional reaction-time competition with physical sensing.

Rather than simply pressing a button, players respond to challenges by presenting colored objects or performing recognized physical actions.

Each Raspberry Pi operates as an independent sensing device while participating in a shared multiplayer session.

The goal is to respond accurately and quickly enough to win rounds and accumulate the highest score.

## C.2 User Experience

The intended interaction proceeds through several stages:

**1. Lobby**

Each Raspberry Pi launches NEON RACE and connects to the shared MQTT session. Players wait for the host to begin the match.

**2. Challenge**

The host coordinates a challenge, such as showing a particular color or performing a supported physical gesture.

**3. Physical Response**

Players respond using their own connected sensors.

**4. Detection**

Each Raspberry Pi processes its sensor input locally and determines whether the requested action has been completed.

**5. Multiplayer Result**

The game communicates completion information through MQTT, determines the round outcome, and updates the shared match state.

**6. Final Result**

After the configured rounds, the game displays the match results.

This interaction makes network communication visible through physical actions and synchronized feedback.

## C.3 Hardware and Software

The project was developed for a three-person team using Raspberry Pis.

Our working prototype incorporated the following components:

| Component | Function |
|---|---|
| Raspberry Pi | Runs the game application and handles networking |
| miniPiTFT display | Displays game states, instructions, and feedback |
| APDS-9960 sensor | Detects colors and proximity-based inputs |
| USB webcam | Supports camera-based gesture recognition when available |
| MQTT broker | Distributes multiplayer messages |
| Python | Implements sensing, interaction logic, and game behavior |
| MediaPipe | Supports hand-gesture processing |
| OpenCV | Provides camera access and image processing |

The APDS-9960 enabled sensor-based interaction without requiring a camera for every challenge.

Camera-based gesture recognition provided an additional interaction method where a working webcam was available.

## C.4 Distributed System Architecture

```text
                 GAME HOST
             Raspberry Pi / PiTFT
                       |
               Game Coordination
                       |
                       v
                 MQTT Broker
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Player 1     Player 2     Player 3
          |            |            |
       Sensors      Sensors      Sensors
          |            |            |
          v            v            v
     Local Input   Local Input   Local Input
      Detection     Detection     Detection
          |            |            |
          +------------+------------+
                       |
                       v
                MQTT Messages
                       |
                       v
              Shared Game State
                       |
                       v
               Round Results
```

The system separates two responsibilities:

**Local computation:** Each Raspberry Pi acquires sensor readings and interprets physical input.

**Distributed coordination:** MQTT allows the devices to exchange game events and maintain a shared multiplayer interaction.

This separation is important because processing raw sensor data centrally would introduce unnecessary network traffic and increase dependence on network performance.

Instead, each device can perform local sensing and transmit the resulting game information.

## C.5 MQTT Communication

NEON RACE used a shared team namespace to coordinate its multiplayer session.

Our player configuration used:

```text
IDD/ct-neon/race
```

The team identifier ensured that participating devices joined the same game rather than an unrelated MQTT session.

The implementation used MQTT to communicate game-related information between the participating Raspberry Pis.

The main categories of information included:

- Player presence and session coordination
- Game challenges and state changes
- Sensor-based completion events
- Round outcomes and scores

The exact message handling and topic structure are implemented in the source code linked below.

## C.6 Software Implementation

The team used a Python implementation integrating physical sensing, graphical output, and multiplayer communication.

### Source Files

**[View NEON RACE Python implementation](media/neon_race/code/neon_race.py)**

**[View NEON RACE dependencies](media/neon_race/code/requirements-neon.txt)**

The application includes several important responsibilities.

**Sensor initialization:** Establishes connections to supported hardware and determines available input capabilities.

**Local interpretation:** Converts camera and sensor measurements into recognized interaction events.

**MQTT communication:** Connects the player to the shared broker and exchanges multiplayer messages.

**Game state management:** Coordinates the lobby, challenge sequence, results, and scoreboard.

**Display feedback:** Presents game information on the Raspberry Pi's miniPiTFT screen.

### Running the Game

After installing the dependencies in a Python virtual environment, a participating Raspberry Pi can launch the application with a player name and shared team identifier.

Example player command:

```bash
python neon_race.py --name pi2 --team ct-neon
```

Example host command:

```bash
python neon_race.py --host --name pi1 --team ct-neon
```

The host and players must use the same team identifier.

The application also supports configurations that exclude camera input when the webcam is unavailable.

## C.7 Development and Integration Process

Our implementation involved several stages of testing and troubleshooting.

### Stage 1: Establishing Network Communication

We first verified MQTT functionality during Part A.

This provided confidence that the Raspberry Pi could communicate through the course broker before introducing the additional complexity of multiplayer gameplay.

### Stage 2: Validating Physical Sensor Input

During Part B, we successfully demonstrated RGB sensing through the APDS-9960 and the shared pixel grid.

This established that physical color measurements could be translated into networked interactions.

### Stage 3: Integrating NEON RACE

For Part C, our team adopted the NEON RACE implementation and configured the participating Raspberry Pis with matching MQTT team identifiers.

We installed the required Python dependencies in isolated virtual environments to avoid interfering with the Raspberry Pi's system Python installation.

We also tested camera initialization and investigated compatibility issues with USB webcams and gesture-recognition dependencies.

### Stage 4: Camera Troubleshooting

During initial testing, one Raspberry Pi reported that its USB webcam could not be opened.

After reconnecting the camera and restarting the application, MediaPipe initialization progressed further.

This highlighted the importance of verifying hardware availability before launching a multiplayer session.

The system's ability to use color and proximity inputs provided a useful alternative when camera-based interaction was unavailable.

### Stage 5: Multiplayer Demonstration

The original design targeted three active Raspberry Pis.

However, one teammate experienced a PiTFT display malfunction during integration, preventing that device from participating fully.

After consulting DTA Albert, we proceeded with an approved two-player demonstration.

This allowed us to validate a working multiplayer interaction while documenting the hardware limitation that prevented the intended three-player demonstration.

## C.8 Final Demonstration

**[Watch NEON RACE Multiplayer Demonstration](media/neon_race/video/Neon_Race_Video_Demonstration.md)**

The recording documents the functional two-player version of NEON RACE.

It demonstrates the physical Raspberry Pi interface and the coordinated multiplayer interaction.

Although the original concept was designed for three players, the final working demonstration involved two active devices because of the third device's display malfunction.

The video provides evidence of the functional prototype and the interaction achieved during testing.

## C.9 User Testing

The assignment requested testing with at least two participants who were not members of the development team.

Our intended external testing was constrained by the limited number of students remaining in the classroom when the prototype became operational.

During the available class time, we prioritized troubleshooting the hardware, establishing reliable multiplayer communication, and capturing a functional demonstration.

As a result, we did not complete two independent non-team user-testing sessions.

This is a limitation of our evaluation rather than evidence that the system has been validated with unfamiliar users.

### Future User-Testing Plan

A subsequent evaluation would involve two or more participants unfamiliar with NEON RACE.

We would investigate:

- **Expectations:** What do participants believe the game will require before receiving instructions?
- **Challenge clarity:** Can participants understand the requested actions immediately?
- **Sensor reliability:** Do the sensors recognize the intended actions consistently?
- **Feedback:** Can players identify when they have completed a challenge and who won?
- **Improvements:** What would participants change about the controls, timing, or game presentation?

These observations would help distinguish implementation reliability from actual usability.

## C.10 Reflection

### What Worked Well?

The most successful aspect of NEON RACE was turning independent Raspberry Pis into a shared multiplayer experience.

The combination of physical sensor input, local computation, MQTT communication, and visual feedback created a more interactive demonstration than a conventional messaging test.

The APDS-9960 also proved useful across multiple parts of the assignment, first contributing RGB measurements to the collaborative grid and then supporting physical game interactions.

### What Were the Main Challenges?

The largest challenge was coordinating several hardware and software components simultaneously.

A device could successfully connect to MQTT while still encountering a problem with its camera, display, or sensor initialization.

We encountered webcam initialization issues and a PiTFT malfunction that reduced the final demonstration from three participating Pis to two.

These challenges reinforced the importance of testing individual subsystems before attempting full integration.

### How Did Sensor Events Work?

The Raspberry Pi collected physical input through its available sensors.

The application interpreted these measurements locally to determine whether an interaction matched a game challenge.

Relevant game events were then communicated through MQTT, allowing other devices to respond to the shared game state.

This approach reduced the need to transmit raw camera imagery between devices.

### Where Did Computation Happen, and Why?

Sensor acquisition and interpretation occurred locally on the Raspberry Pis.

Multiplayer coordination used MQTT messaging, allowing the devices to communicate without directly sharing raw sensor streams.

This division supported a more modular architecture, where each Raspberry Pi was responsible for interpreting its own physical environment.

The design also supported privacy by keeping camera frames on the local device rather than transmitting them through MQTT.

### What Would We Improve?

Our first priority would be restoring reliable three-device participation and testing the complete intended configuration.

Additional improvements would include more robust camera detection, better sensor calibration across different lighting conditions, clearer connection-status feedback, and improved recovery when a device disconnects.

We would also conduct structured external user testing to determine whether the game is intuitive for people unfamiliar with its implementation.

For a competitive reaction game, it would be valuable to investigate the effects of MQTT latency and differences in sensor processing time on round outcomes.

## C.11 Team Collaboration and AI Assistance

NEON RACE was developed collaboratively, with team members contributing to the concept, implementation, integration, and testing.

The project incorporated team-generated Python code and iterative troubleshooting across the participating Raspberry Pis.

AI assistance was used during development for brainstorming, understanding MQTT architecture, preparing setup instructions, troubleshooting Python environments and hardware initialization, and organizing documentation.

The final hardware testing and recorded multiplayer demonstration were performed by the team.

---

# Final Deliverables

| Deliverable | Documentation |
|---|---|
| Part A: MQTT publisher and subscriber | [MQTT test screenshots](media/mqtt_tests/) |
| Part B: Collaborative pixel grid | [Sensor and grid images](media/part_b_images/) |
| Part C: NEON RACE source code | [Python implementation](media/neon_race/code/neon_race.py) |
| Part C: Python dependencies | [Requirements](media/neon_race/code/requirements-neon.txt) |
| Part C: Multiplayer video | [Video demonstration](media/neon_race/video/Neon_Race_Video_Demonstration.md) |

## Conclusion

Lab 6 demonstrated how multiple Raspberry Pis can communicate and coordinate physical interactions using MQTT.

We progressed from a simple publish/subscribe test to a collaborative color-sensing grid, and finally to NEON RACE, a multiplayer reaction game combining local sensing with distributed communication.

The final two-player demonstration showed the potential of the system while revealing practical challenges associated with coordinating multiple hardware devices.

The project strengthened our understanding of publish/subscribe communication, distributed computation, physical interaction design, and the importance of robust hardware integration.
