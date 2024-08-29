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

## Lecture 2.1
