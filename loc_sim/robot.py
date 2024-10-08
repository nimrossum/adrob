import pygame
#from sensors import CompassSensor  # Import the LidarSensor class
import math
import random
import numpy as np


class DifferentialDriveRobot:
    def __init__(self, x, y, theta, image_path, axl_dist=5, wheel_radius=2.2):
        self.x = x
        self.y = y
        self.theta = theta  # Orientation in radians
        self.axl_dist = axl_dist
        self.wheel_radius = wheel_radius
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.currently_turning = 0
        self.angular_velocity = 0
        self.linear_velocity = 0

        self.landmarks = []
        self.left_motor_speed = 0
        self.right_motor_speed = 0
        self.compass = CompassSensor()
        self.odometry_weight = 0.0
        self.odometry_noise_level = 0.01

        self.loc_history = []

    def predict(self, delta_time):
        self.move(delta_time)
        # Update orientation (theta) using the robot's compass sensor
        #compass_heading = self.compass.read_compass_heading(self.theta,self.angular_velocity, delta_time)

        # Blend odometry and compass headings
        #blended_heading = (self.odometry_weight * self.theta) + ((1-self.odometry_weight) * compass_heading)

        # Update the robot's orientation
        #self.theta = blended_heading

        if len(self.loc_history) > 1_000:
            self.loc_history.pop(0)

        self.loc_history.append((self.x, self.y))

        return RobotPose(self.x, self.y, self.theta)

    def move(self, delta_time):


        # Assume maximum linear velocity at motor speed 500
        v_max = 10  # pixels/second

        # Calculate the linear velocity of each wheel
        left_wheel_velocity = (self.left_motor_speed / 500) * v_max
        right_wheel_velocity = (self.right_motor_speed / 500) * v_max

        v_x = math.cos(self.theta) * (self.wheel_radius * (left_wheel_velocity + right_wheel_velocity) / 2)
        v_y = math.sin(self.theta) * (self.wheel_radius * (left_wheel_velocity + right_wheel_velocity) / 2)
        omega = (self.wheel_radius * (left_wheel_velocity - right_wheel_velocity)) / (2 * self.axl_dist)

        self.x += (v_x * delta_time)
        self.y += (v_y * delta_time)
        self.theta += (omega * delta_time)

        # Ensure the orientation is within the range [0, 2*pi)
        #self.theta = self.theta % (2 * math.pi)

        # Add a small amount of noise to the orientation
        #noise = random.gauss(0, self.odometry_noise_level)
        #self.theta += noise

    def set_motor_speeds(self, left_motor_speed, right_motor_speed):
        self.left_motor_speed = left_motor_speed
        self.right_motor_speed = right_motor_speed


    def get_robot_position(self):
        return RobotPose(self.x, self.y, self.theta)

    def update_estimated_position(self, estimated_pose):
        self.x = estimated_pose.x
        self.y= estimated_pose.y
        self.theta = estimated_pose.theta

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, math.degrees(-1*self.theta))
        self.rect.center = (int(self.x), int(self.y))
        new_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, new_rect)

         # Calculate the left and right wheel positions
        half_axl = self.axl_dist
        left_wheel_x = self.x - half_axl * math.sin(self.theta)
        left_wheel_y = self.y + half_axl * math.cos(self.theta)
        right_wheel_x = self.x + half_axl * math.sin(self.theta)
        right_wheel_y = self.y - half_axl * math.cos(self.theta)

        # Calculate the heading line end point
        heading_length = 15
        heading_x = self.x + heading_length * math.cos(self.theta)
        heading_y = self.y + heading_length * math.sin(self.theta)

        # Draw the axle line
        pygame.draw.line(surface, (0, 255, 0), (left_wheel_x, left_wheel_y), (right_wheel_x, right_wheel_y), 3)

        # Draw the heading line
        pygame.draw.line(surface, (255, 0, 0), (self.x, self.y), (heading_x, heading_y), 3)

        # Draw previous locations
        for loc in self.loc_history:
            pygame.draw.circle(surface, (0, 0, 255), (int(loc[0]), int(loc[1])), 1)


    def getMotorspeeds(self):
        return (self.left_motor_speed, self.right_motor_speed)

    #Exercise 6.1 make the robot explore the environment.
    #Exercise 6.2 make the robot avoid the walls using lidar sensor data
    def explore_environment(self, lidar_scans):

        if len(lidar_scans) < 60:
            print("no data from lidar yet")
            return

        sensor_steps_for_front_array = int((len(lidar_scans) / 4) / 3)
        self.front_sensor_array = [
            lidar_scans[2 * sensor_steps_for_front_array],
            lidar_scans[sensor_steps_for_front_array],
            lidar_scans[0],
            lidar_scans[len(lidar_scans) - sensor_steps_for_front_array],
            lidar_scans[len(lidar_scans) - 2 * sensor_steps_for_front_array]
        ]

        self.left_sensor = lidar_scans[int((len(lidar_scans) / 4) * 3)]
        self.front_left_sensor_1 = lidar_scans[len(lidar_scans) - 2 * sensor_steps_for_front_array + 1]
        self.back_sensor = lidar_scans[int(len(lidar_scans) / 2)]
        self.right_sensor = lidar_scans[int(len(lidar_scans) / 4)]
        self.front_right_sensor_1 = lidar_scans[2 * sensor_steps_for_front_array - 1]

        # print(f"l:{left_sensor}, fl1:{front_left_sensor_1}, b:{back_sensor}, fr1:{front_right_sensor_1}, r:{right_sensor}")
        # This is not readable, we will print it with padded spaces to make it more readable:
        print(f"l:{self.left_sensor:5.2f}, fl1:{self.front_left_sensor_1:5.2f}, b:{self.back_sensor:5.2f}, fr1:{self.front_right_sensor_1:5.2f}, r:{self.right_sensor:5.2f}")


        #Exercise 6.1 modify this to control the robot
        #Exercise 6.2 use your exploration algorithm from previous exercise if you have it.

        sum = 0

        for i in range(0, len(self.front_sensor_array)):
            sum += self.front_sensor_array[i]



        d_left, d_top_left, d_center, d_top_right, d_right = self.front_sensor_array

        speed_factor = 10 + sum / 10

        if d_center > 50:
            self.set_motor_speeds(15 * speed_factor + (5 * speed_factor)*random.random(), 15 * speed_factor + (5 * speed_factor)*random.random())
        elif d_left > d_right:
            self.set_motor_speeds(20 * speed_factor, speed_factor)
        else:
            self.set_motor_speeds(speed_factor, 20 * speed_factor)


class CompassSensor:

    drift_rate=0.0001
    USE_DRIFT=False

    def __init__(self, noise_stddev=0.0001) -> None:
        self.noise_level = noise_stddev

    def read_compass_heading(self, start_heading, angular_velocity, delta_time):
         # Update orientation (theta) based on angular velocity
        start_heading += angular_velocity * delta_time

        # Ensure the orientation is within the range [0, 2*pi)
        start_heading = start_heading % (2 * math.pi)

        # Add a small amount of noise to the orientation
        noise = random.gauss(0, self.noise_level)
        start_heading += noise

        # Introduce a small constant angular drift
        if self.USE_DRIFT:
            drift = self.drift_rate * delta_time
            start_heading += drift

        # Return the updated theta in radians
        return start_heading

class RobotPose:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
    #this is for pretty printing
    def __repr__(self) -> str:
        return f"x:{self.x},y:{self.y},theta:{self.theta}"
