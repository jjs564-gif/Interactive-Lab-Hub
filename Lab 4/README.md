# Lab 4: Ph-UI!!!

**Student:** Jonathan Sharpy  
**Cornell Tech | Developing and Designing Interactive Devices**  
**Project:** WasteWise

---

## Part 1: Sensing and Actuation Exploration

### Sensor and Actuator Testing

Before developing WasteWise, I explored several sensing and actuation components using the Raspberry Pi 5. The tests included capacitive touch sensing, proximity detection, RGB/color sensing, gesture recognition, and servo motor control.

The setup photographs and screenshots of the corresponding terminal outputs are organized in the [Sensor and Actuator Testing Evidence](media/sensor_tests/) folder.

| Component | Test Evidence |
|---|---|
| MPR121 capacitive touch | [Setup](media/sensor_tests/Capacitive_Touch_MPR121_Setup.jpeg) · [Terminal output](media/sensor_tests/Capacitive_Touch_MPR121_Terminal_Output.png) |
| APDS-9960 proximity | [Terminal output](media/sensor_tests/Proximity_APDS9960_Terminal_Output.png) |
| APDS-9960 color/light | [Terminal output](media/sensor_tests/Color_Light_APDS9960_Terminal_Output.png) |
| APDS-9960 gesture | [Terminal output](media/sensor_tests/Gesture_APDS9960_Terminal_Output.png) |
| Servo motor and Servo pHAT | [Setup](media/sensor_tests/Servo_pHAT_Setup.jpeg) · [Terminal output](media/sensor_tests/Servo_Motor_Terminal_Output.png) |

The servo was first tested independently before being incorporated into the WasteWise cardboard prototype.

**Testing observations:**

- **Capacitive touch:** The MPR121 detected touch events on its electrode contacts and displayed the corresponding messages in the terminal.
- **Proximity:** The APDS-9960 proximity readings changed as objects moved closer to or farther from the sensor.
- **Color/light:** The APDS-9960 produced different RGB and light readings when exposed to different surfaces and lighting conditions.
- **Gesture:** The APDS-9960 detected directional hand gestures, including left, right, and up.
- **Servo actuation:** The SparkFun Servo pHAT successfully controlled the servo motor's angular position, demonstrating repeatable physical movement.

These tests helped establish which sensing and actuation capabilities could support the physical interaction concepts explored below.

---

## Physical Interaction Design: Feast Automata

### Five Design Sketches

I explored five dining-related concepts that combine sensing and actuation to create playful or useful physical interactions.

The sketches illustrate different physical arrangements, including the placement of sensors, actuators, and other components relative to the user and dining environment.

**1. WasteWise: Plate Scanner**

A distance sensor observes food remaining on a plate. A servo-driven hand provides a thumbs-up or thumbs-down gesture to communicate feedback about food waste.

**2. CookCue: Food Readiness Assistant**

A color sensor examines the surface appearance of food during cooking. A speaker provides feedback about its appearance or cooking progress. Color alone would not be used to establish food safety.

**3. SpoonSense: Utensil Advisor**

A sensor or user input identifies characteristics of the food, such as temperature or type. A physical indicator recommends an appropriate utensil material.

**4. CleanSwipe: Automatic Utensil Cleaner**

A proximity sensor detects when a utensil enters a tabletop cleaning mechanism. A servo moves a cleaning component across the utensil's surface.

**5. UtensilCarousel: Smart Utensil Selector**

A rotary encoder or joystick allows users to select a dining task or food type. A servo-driven carousel rotates to present the appropriate utensil.

**Five concept sketches:**

<img width="1227" height="815" alt="Five physical interaction design sketches" src="https://github.com/user-attachments/assets/5e0539da-3f4d-44d5-b8e0-2b7da6104ea6" />

### Questions Raised by the Sketches

The five sketches explore different ways to use sensing and physical feedback to improve everyday dining experiences.

The main questions they raise are:

- **WasteWise:** Can a distance sensor reliably distinguish leftover food from an empty plate? Where should it be positioned, and would a physical thumbs-up or thumbs-down gesture effectively communicate food waste?
- **CookCue:** Can food color provide useful information about cooking progress, and how should the device communicate its assessment without implying that color alone guarantees food safety?
- **SpoonSense:** Can temperature and food characteristics help recommend a more comfortable utensil material?
- **CleanSwipe:** How could a compact tabletop mechanism clean a utensil between foods without interrupting the meal? How would it avoid transferring contaminants?
- **UtensilCarousel:** Can a rotating utensil holder make selecting the appropriate utensil more convenient, and how much space would it occupy on the table?

To investigate these questions, I would prototype the physical placement of the sensors, the size and movement of the actuators, and how users interact with each device during a meal.

For WasteWise specifically, I wanted to test whether a simple rotating cardboard hand could provide recognizable feedback before attempting a more complex sensing and actuation system.

---

### Selected Design: WasteWise

I selected **WasteWise**, a device designed to encourage people to reduce food waste by providing immediate physical feedback about leftovers on their plates.

I chose this concept because it addresses an everyday problem while offering a straightforward interaction between sensing and actuation. The intended system uses distance sensing to estimate how much food remains on a plate, then responds with a physical gesture.

My original idea involved two mechanical hands clapping to celebrate minimal food waste. However, I simplified the mechanism to a single rotating hand that could display a thumbs-up or thumbs-down. This reduced the mechanical complexity while preserving the central idea of communicating feedback through physical movement.

For the low-fidelity prototype, I attached a cardboard hand to a servo motor and used a manually triggered rotation to demonstrate the intended interaction. This allowed me to focus on testing the clarity and feasibility of the physical feedback before integrating automatic food detection.

---

### Low-Fidelity Prototype

I constructed a physical WasteWise prototype using a cardboard hand, a micro-servo motor, the SparkFun Pi Servo pHAT, and a Raspberry Pi 5.

The cardboard hand was attached to the servo horn, allowing the motor to rotate the gesture between different orientations.

For this initial prototype, I focused on demonstrating the physical feedback mechanism rather than constructing a complete housing or implementing automatic food detection.

**Prototype photographs**

**1. WasteWise prototype assembly**

<img width="1536" height="2048" alt="WasteWise prototype assembly" src="https://github.com/user-attachments/assets/15b52ad7-6fb9-4241-9b29-6f9d952efee8" />

**2. Servo horn and cardboard attachment**

<img width="1536" height="2048" alt="Servo horn attachment" src="https://github.com/user-attachments/assets/fbfb1160-04a6-41e7-b208-9aa7cee048a7" />

**3. Cardboard thumbs-up prototype**

<img width="1536" height="2048" alt="Cardboard thumbs-up prototype" src="https://github.com/user-attachments/assets/983c9a08-b1a7-40d9-9fb0-7e97fd98493f" />

---

### Wizard-of-Oz Demonstration

**[Watch the WasteWise Prototype Demonstration](https://drive.google.com/file/d/12jNM7uuJcP61YKrk7G9qeKD65bir73ut/view?usp=sharing)**

The video demonstrates the intended interaction between detecting leftover food and providing physical feedback.

I first position the distance sensor over a plate containing leftover food. When the sensor is moved over the leftovers, I manually trigger the servo motor by pressing the spacebar on my laptop.

The servo rotates the cardboard hand downward, displaying a thumbs-down gesture to represent food waste.

This is a **Wizard-of-Oz prototype**: the intended sensing interaction is simulated by the operator, while the servo motor's physical movement is real.

---

### Prototype Implementation

I created a cardboard thumbs-up cutout and attached it to the horn of a micro-servo motor connected to the SparkFun Pi Servo pHAT and Raspberry Pi 5.

Using a Python script, I calibrated the servo to rotate between approximately **60° and 150°**. Pressing the spacebar activates the rotation, turning the cardboard thumbs-up into a thumbs-down.

For the Wizard-of-Oz demonstration, I positioned a distance sensor above a plate containing leftover food. When the sensor was positioned over the leftovers, I manually pressed the spacebar to trigger the servo, producing a thumbs-down gesture to represent detected food waste.

The sensing-to-actuation connection was simulated rather than automated. This prototype demonstrates the intended physical interaction, while automatic leftover detection and quantitative food-waste estimation remain goals for future development.

**Prototype code:** [wastewise_demo.py](wastewise_demo.py)

---

## AI Assistance Acknowledgment

I used ChatGPT as a technical and documentation assistant during this lab.

AI assistance included guidance with Raspberry Pi setup, Python environment configuration, sensor and servo testing, troubleshooting, and development of the keyboard-controlled servo demonstration script.

I also used ChatGPT to help organize and refine my written documentation and to guide creation of my visual references based on my five original dining concepts.

The concept selection, design decisions, cardboard prototype construction, hardware testing, servo calibration, demonstration recording, and final design sketches were completed by me. The Wizard-of-Oz demonstration and its simulated sensing behavior are explicitly identified in the documentation.

---

## Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

---

### Part E

#### Build & Integrate: Sensing + Actuation

For Part 2, build the Feast Automata interaction you developed in Part D by connecting sensing/input to physical actuation.

**Your prototype should:**
- Use at least one sensing or input device.
- Use servo-based physical actuation.
- Connect sensing and actuation into a meaningful interaction around eating, drinking, cooking, serving, or sharing food.
- Additional inputs, displays, LEDs, buttons, or other outputs are optional extensions.

**Document your system with:**
- Code for your sensing + actuation prototype
- Photos and/or video of the working prototype in action
- A simple interaction diagram or sketch showing how sensing and actuation are connected
- Written reflection: What did you learn about connecting sensing, movement, and physical form? What was fun, surprising, or challenging?

**Questions to consider:**
- How does your chosen sensor or input shape the physical response?
- How does the physical arrangement of the sensor and actuator change the interaction?
- What thresholds, timing, or movement patterns make the interaction feel clear or playful?
- What changes when you adjust the sensor placement or servo motion?

Iterate on the sensing, movement, and physical form, and document what you discover.

See encoder_accel_servo_dashboard.py in the Lab 4 folder for an optional example of chaining together three devices.

**`Lab 4/encoder_accel_servo_dashboard.py`**

#### Example Application: Windmill Coaster

Now that you have explored both sensing and actuation, here is a simple example that combines the two.

The **Windmill Coaster** uses a Qwiic distance/proximity sensor to detect when a cup is placed on a coaster. When the cup is detected, a servo motor animates a small windmill by sweeping it back and forth, turning an ordinary action during drinking into a playful physical interaction.

<p align="center">
    <img src="windmill_coaster11.gif" alt="Windmill Coaster Demo" width="400"/>
</p>


This example demonstrates a simple interaction pipeline:

**cup placed → distance sensor detects cup → servo actuates windmill**

Connect the Qwiic distance sensor to the Pi and connect the servo to Channel 0 of the Servo pHAT. Make sure the Servo pHAT is powered through its USB-C connection.

Run the example script:

```bash
python windmill_coaster.py
```

The script continuously reads the proximity value from the distance sensor. When the value passes a threshold, the servo begins animating the windmill. When the cup is removed, the servo stops and returns to its resting position.

You may need to adjust `CUP_THRESHOLD` in [`windmill_coaster.py`](windmill_coaster.py) depending on the size of your cup and the physical placement of the sensor. You can run `qwiic_distance.py` first to compare readings with and without a cup.

Use this example as a starting point. Change the sensor, movement, physical form, or dining interaction to create your own Feast Automata variation.

#### Optional Extensions

The following examples are optional resources if you want to add more inputs or outputs to your prototype.

##### Using Multiple Qwiic Buttons: Changing I2C Address (Physically & Digitally)

If you want to use more than one Qwiic Button in your project, you must give each button a unique I2C address. There are two ways to do this:

##### 1. Physically: Soldering Address Jumpers

On the back of the Qwiic Button, you'll find four solder jumpers labeled A0, A1, A2, and A3. By bridging these with solder, you change the I2C address. Only one button on the chain can use the default address (0x6F).

**Address Table:**

| A3 | A2 | A1 | A0 | Address (hex) |
|----|----|----|----|---------------|
|  0 |  0 |  0 |  0 |    0x6F       |
|  0 |  0 |  0 |  1 |    0x6E       |
|  0 |  0 |  1 |  0 |    0x6D       |
|  0 |  0 |  1 |  1 |    0x6C       |
|  0 |  1 |  0 |  0 |    0x6B       |
|  0 |  1 |  0 |  1 |    0x6A       |
|  0 |  1 |  1 |  0 |    0x69       |
|  0 |  1 |  1 |  1 |    0x68       |
|  1 |  0 |  0 |  0 |    0x67       |
| ...| ...| ...| ... |     ...      |

For example, if you solder A0 closed (leave A1, A2, A3 open), the address becomes 0x6E.

**Soldering Tips:**
- Use a small amount of solder to bridge the pads for the jumper you want to close.
- Only one jumper needs to be closed for each address change (see table above).
- Power cycle the button after changing the jumper.

##### 2. Digitally: Using Software to Change Address

You can also change the address in software (temporarily or permanently) using the example script `qwiic_button_ex6_changeI2CAddress.py` in the Lab 4 folder. This is useful if you want to reassign addresses without soldering.

Run the script and follow the prompts:
```bash
python qwiic_button_ex6_changeI2CAddress.py
```
Enter the new address (e.g., 5B for 0x5B) when prompted. Power cycle the button after changing the address.

**Note:** The software method is less foolproof and you need to make sure to keep track of which button has which address!


##### Using Multiple Buttons in Code

After setting unique addresses, you can use multiple buttons in your script. See these example scripts in the Lab 4 folder:

- **`qwiic_1_button.py`**: Basic example for reading a single Qwiic Button (default address 0x6F). Run with:
	```bash
	python qwiic_1_button.py
	```

- **`qwiic_button_led_demo.py`**: Demonstrates using two Qwiic Buttons at different addresses (e.g., 0x6F and 0x6E) and controlling their LEDs. Button 1 toggles its own LED; Button 2 toggles both LEDs. Run with:
	```bash
	python qwiic_button_led_demo.py
	```

Here is a minimal code example for two buttons:
```python
import qwiic_button

# Default button (0x6F)
button1 = qwiic_button.QwiicButton()
# Button with A0 soldered (0x6E)
button2 = qwiic_button.QwiicButton(0x6E)

button1.begin()
button2.begin()

while True:
		if button1.is_button_pressed():
				print("Button 1 pressed!")
		if button2.is_button_pressed():
				print("Button 2 pressed!")
```

For more details, see the [Qwiic Button Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-button-hookup-guide/all#i2c-address).

---

##### PCF8574 GPIO Expander: Add More Pins Over I²C

Sometimes your Pi’s header GPIO pins are already full (e.g., with a display or HAT). That’s where an I²C GPIO expander comes in handy.

We use the Adafruit PCF8574 I²C GPIO Expander, which gives you 8 extra digital pins over I²C. It’s a great way to prototype with LEDs, buttons, or other components on the breadboard without worrying about pin conflicts—similar to how Arduino users often expand their pinouts when prototyping physical interactions.

**Why is this useful?**
- You only need two wires (I²C: SDA + SCL) to unlock 8 extra GPIOs.
- It integrates smoothly with CircuitPython and Blinka.
- It allows a clean prototyping workflow when the Pi’s 40-pin header is already occupied by displays, HATs, or sensors.
- Makes breadboard setups feel more like an Arduino-style prototyping environment where it’s easy to wire up interaction elements.

**Demo Script:** `Lab 4/gpio_expander.py`

<p align="center">
    <img src="gpio_leds.gif" alt="GPIO Expander LED Demo" width="400"/>
</p>

We connected 8 LEDs (through 220 Ω resistors) to the expander and ran a little light show. The script cycles through three patterns:
- Chase (one LED at a time, left to right)
- Knight Rider (back-and-forth sweep)
- Disco (random blink chaos)

Every few runs, the script swaps to the next pattern automatically:
```bash
python gpio_expander.py
```

This is a playful way to visualize how the expander works, but the same technique applies if you wanted to prototype buttons, switches, or other interaction elements. It’s a lightweight, flexible addition to your prototyping toolkit.

---


---

---

### Part F

### Final Documentation

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

---

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.
