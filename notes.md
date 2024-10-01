# Lecture 1.1: Introduction to Robotics - Tuesday, 27/08/2024

Literature:
-
- We will use a third of the Murphy book

The course

- Theory light
- First 3-4 weeks: bootcamp, fundamentals
- A few sections from the book
- Reinforcement learning

Weeks:
- Tuesday: Kasper Entertain for 2 hours + building fo 2 hours
- Thursday: Kasper Entertain for 1 hour + building for 3 hours

More time should be spend on building outside of class hours.

**Exam:**
- Three project during the course
- Write a report about the project with feedback about what to change

- The final report is submitted as the exam
- The exam is oral where we talk about the project
- Some questions about the topics covered in the course

## Origin of Robotics

- Rossum's Universal Robots (1920)
- Robbie (1939)
- Runaround (1942)

Asimov's laws of robotics:

1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must project its own existence as long as such protection does not conflict with the First or Second Law.

In most movies, robots are evil. Like the Terminator.

## Robots from the Industrial Revolution

- Power loom (1733)
- Steam engine (1760)
- Worm gear (1774)
- Mass production (1908)
- Henry Ford's car factory

First robot introduced at General Motors in 1961.

## Basics

- Make the robot body fit the task as much as possible, then you will need as little intelligence as possible.

## Mobile Robots

Mobile Industrial Robots Odense - Regnar
- Was removed because the elderly were scared of the robot
- Safety issues at Herlev (going around corners)

- The human aspect is very important: How will the robot fit into our world?

- Underwater robots does not need to fight gravity, so they can swim around for a long time

- Scarlet Knight was a submarine robot that crossed the pacific ocean from New Jersey to Balona, Spain

## Exercises

Task 1: Build a robot that can move to a certain spot and a specific orientation.



Group 4 / JoMaMa

## Lecture 1.2 - Thursday, 29/08/2024

What you have to worry about when solving the task:
- Precision
- Control
- Model: the model of the world
  - Precision of measurements
- Environment: external factors that affect the robot
- Actuator noise: the actuators are not perfect and will not always do exactly what you tell it to
- Mechanics of the robot: the robot is not perfect, wheels might compress and affect your model
  - Actuator type
  - Play / wiggle room of the mechanics
- More resolution: how precisely can you control the motor?
  - Smaller wheels will give you more resolution
- Power source
  - Do we give the robot the correct amount of power?
- Sampling rate
  - How often can the robot get new instructions?
- Inertia
  - How fast can the robot change direction?
  - Controlled by weight and speed

## Lecture 2.1 - Tuesday, 03/09/2024



# Lecture 2.2 - Thursday, 05/09/2024

## Behavior based control

Classic control: Sense $\rightarrow$ Plan $\rightarrow$ Act

Behavior based control: Perception $\rightarrow$ Response

- We can build a robot by combining simple behaviors

Example: Roomba

Behaviors:
- Spiraling
- Wall following
- Room crossing (ant line, random walk)
- Dirt detection

Sensors:
- Cliff sensor (IR) - detects the edge of a cliff
  - Limitations: Couldn't clean black carpets, as the robot thought it was a cliff
- Virtual Wall / Home base: Infrared light that the robot can detect to get back to the charging station
- Wall: Infrared light that the robot can detect to follow the wall
- Wheel drop sensors: Detects if the robot is stuck or if the wheels are not touching the ground or if the robot is picked up
  - Very simple and reliable, just a switch
- Bump: Detects if the robot has bumped into something
  - Big plastic bumper that pushes in when it hits something
- Odometry: Encoders on the wheels to measure how far the robot has moved
- Dirt: Acoustic impact sensor (noise)

## Simple behaviors

Simple is always better
- Robust
- Cheap
- Easy to understand
- No goal
- Can be just a few lines of code

Should the robot close its eyes when turning in an intersection?
- Maybe, to avoid interference from the behaviors

Behaviors are modular

## Behavior coordination

- They cannot all control the robot at the same time
- Should they compete or cooperate?
  - Compete: The strongest behavior wins
  - Cooperate: The behaviors can work together

- A competitive method: Priority based coordination: The behaviors are ordered by priority

- Action-selector coordination: Over time, coordinate which behavior is more important

- Voting based coordination: Each behavior votes on what to do
  - If most behaviors vote for the same action, that action is taken

- Fusion-based coordination: Fuse the responses
  - If one behavior says to go left, and another says to go right, the robot goes straight (vector addition)


1. Build a minimal robot system
2. Evaluate the robot
3. Add new behaviors or adjust
  - Software, robot design, sensor locations etc.
4. Evaluate the robot
5. Repeat

## Complex systems

Kismet example

Social human robot

# Lecture 3.1 - Tuesday 10/09/2024 - Hierarchical architectures

## Symbolic-based paradigm

Stuck for several decades in the mindset that we only need better sensors, our model is perfect and our robot is perfect and the world is perfect.

Finally led to hybrid systems.

# Lecture 3.2 - Thursday 12/09/2024 - Hierarchical architectures

# Lecture 4.1 - Tuesday 17/09/2024

Ask these questions when writing the report

- Which assumptions have we done in the design of the robot?
- Which assumptions are we depending on?

- How are we measuring the performance of the robot?
- How is it replicated?

- Distance between sensors
- Photo of the robot
- Geometry of the robot
- Technical drawing of the robot

- Does the results obtained give a fair and realistic picture of the system being studied?
  - How honest are our results?

- Sometimes we have a tendency to do too large conclusions based on too little data
  - Don't overstate the results
  - Be careful with the conclusions

# Lecture 5.1 - Tuesday 24/09/2024

# Lecture 5.2 - Thursday 26/09/2024

# Lecture 6.1 - Tuesday 01/10/2024

Discretized space: The world is divided into cells

Feature based localization: The robot uses features in the world to localize itself

Problem: The environment is not static

**Belief**: Confidence in the robot's position

What can improve belief?
- Feature extraction
- More sensors

## Particle filtering

- Monte Carlo

- Random sampling



Install pip
```bash
wget https://bootstrap.pypa.io/get-pip.py
