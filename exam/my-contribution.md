# My Contribution to the Project

## My Contribution to the Project

- I have been a part of all aspects of the project
- For the majority of the exam project, my primary focus was worked with programming and developing the physical robot

- My main contributions were:

  - Development of **computer vision** for robot detection
  - Implementation of **stacked behavior-based control** for the robots

- Implemented robot detection using **computer vision** (physical_robot/camera_sensor.py)
  - I implemented **color tracking**

  - I used the **OpenCV** library for image processing
  - I used **image segmentation** using **HSV color space** for detecting the robots LEDs
  - I started by continuing from the tennis ball detection that I developed during class
  - I calibrated the HSV color space to detect blue colors, initially tested with a blue picture on a phone
  - Then I started calibrating it further using a secondary Thymio robot that showed blue color
  - This was done using a script, that created a user interface with sliders for each of the 6 values (lower color, upper color)
  - The values were adjusted until only the contour around the LED was left in the masked frame
  - I then implemented red detection, by changing the HSV color range if the robot type was an avoider

- Implemented **behavior based control** in specific scenarios, due to the limitations of the AvoidModel

  - Due to the **reality gap**, we were not able to provide the AvoidModel with the distance to the nearest wall.
  - Therefore, I implemented a simple behavior that would make the robot turn around if it detected a wall
  - Our avoider did not handle the rules of the safe zone, so I implemented a behavior that would set a timer and leave the safe zone after a certain time
  - For our seeker, I also developed a **Continous Encoded Behavior**. The computer vision system outputted the relative position of a detected avoider robot. This was directly coupled to calculate the motor speeds for the robot. This behavior was used stacked with other behaviors such as wall avoidance behavior and safe zone behavior, using **Priority-based coordination**, meaning that some behaviors overruled others. I incrementally add new behaviors and tested them iteratively (**Experimentally driven**)



- Simplify code by creating all robots using list comprehension
- Project setup (.gitignore, requirements.txt, venv, auto install scripts)
- Safe-zone detection: I implemented the LED representation in the simulation and made it update based on the detected floor
- Kept track of project goals and whether we fulfilled them

## What I learned

- Our learning system used **offline reward-based evolutionary learning**

- We were hindered by **perceptual aliasing**, since we assumed we could know the shortest distance to the closest wall. This was not possible due to the **reality gap**.
