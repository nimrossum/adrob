import shapely
from shapely.geometry import LinearRing, LineString, Point
from numpy import sin, cos, pi, sqrt
from random import random
import time

# A prototype simulation of a differential-drive robot with one sensor

# Constants
###########
wR = 0.02  # radius of wheels in meters
wL = 0.10  # distance between wheels in meters

W = 2.0  # width of arena
H = 2.0  # height of arena

robot_timestep = 0.1  # 1/robot_timestep equals update frequency of robot
simulation_timestep = 0.01  # timestep in kinematics sim (probably don't touch..)

# the world is a rectangular arena with width W and height H
# world = LinearRing([(W / 2, H / 2), (-W / 2, H / 2), (-W / 2, -H / 2), (W / 2, -H / 2)])
world = [
    LinearRing([(W / 2, H / 2), (-W / 2, H / 2), (-W / 2, -H / 2), (W / 2, -H / 2)]),
    # Obstacle
    LinearRing([(0.5, 0.5), (0.5, 0.7), (0.7, 0.7), (0.7, 0.5)]),
]

# Variables
###########

x = 0.0  # robot position in meters - x direction - positive to the right
y = 0.0  # robot position in meters - y direction - positive up
# t = random() * 2 * pi  # robot heading with respect to x-axis in radians
t = 0  # robot heading with respect to x-axis in radians

left_wheel_velocity = 0.5  # robot left wheel velocity in radians/s
right_wheel_velocity = 0.5  # robot right wheel velocity in radians/s


# Kinematic model
#################
# updates robot position and heading based on velocity of wheels and the elapsed time
# the equations are a forward kinematic model of a two-wheeled robot - don't worry just use it
def simulationstep():
    global x, y, t

    for step in range(
        int(robot_timestep / simulation_timestep)
    ):  # step model time/timestep times
        v_x = cos(t) * (wR * left_wheel_velocity / 2 + wR * right_wheel_velocity / 2)
        v_y = sin(t) * (wR * left_wheel_velocity / 2 + wR * right_wheel_velocity / 2)
        omega = (wR * right_wheel_velocity - wR * left_wheel_velocity) / (2 * wL)

        x += v_x * simulation_timestep
        y += v_y * simulation_timestep
        t += omega * simulation_timestep


# Simulation loop
#################
tfile = open("trajectory.dat", "w")
pfile = open("points.dat", "w")

# Measure time it takes to run simulation

start = time.time()

for cnt in range(5_000):
    # 360 degree sensor

    min_laser_distance = (t, 2 * (W + H))

    amount_of_rays = 10
    start_angle = -pi / 2
    end_angle = pi / 2
    band = end_angle - start_angle
    rads_per_ray = (band) / amount_of_rays

    for i in range(amount_of_rays):
        radians = start_angle + i * rads_per_ray

        if cnt == 0:
            tfile.write(
                f"{x}, {y}, {cos(t + radians) * 0.2}, {sin(t + radians) * 0.2}\n"
            )

        laser_ray = LineString(
            [
                (x, y),
                (
                    x + cos(t + radians) * 2 * (W + H),
                    (y + sin(t + radians) * 2 * (W + H)),
                ),
            ]
        )  # a line from robot to a point outside arena in direction of t
        for w in world:
            ls = w.intersection(laser_ray)
            sqrd_dist = (ls.x - x) ** 2 + (ls.y - y) ** 2  # distance to wall
            if sqrd_dist < min_laser_distance[1]:
                min_laser_distance = (t + radians, sqrd_dist)

    # simple single-ray sensor

    ray = LineString(
        [(x, y), (x + cos(t) * 2 * (W + H), (y + sin(t) * 2 * (W + H)))]
    )  # a line from robot to a point outside arena in direction of t

    s = world.intersection(ray)
    distance = sqrt((s.x - x) ** 2 + (s.y - y) ** 2)  # distance to wall

    wall_angle, closest_wall_dist = min_laser_distance

    target_trajectory = wall_angle + pi / 2

    diff_from_target = t - target_trajectory

    # simple controller - change direction of wheels every 10 seconds (100*robot_timestep) unless close to wall then turn on spot

    color = "green"

    if cnt % 50 == 0:
        if closest_wall_dist < 0.1:
            if diff_from_target > 0:
                color = "red"
                print(f"Close to wall, distance is {closest_wall_dist}, turning left")
                left_wheel_velocity = -0.5
                right_wheel_velocity = 0.5
            else:
                color = "blue"
                print(f"Close to wall, distance is {closest_wall_dist} turning right")
                left_wheel_velocity = 0.5
                right_wheel_velocity = -0.5
    if cnt % 200 == 0:
        print("Cruising")
        # left_wheel_velocity = 0.5
        # right_wheel_velocity = 0.5
        left_wheel_velocity = random()
        right_wheel_velocity = random()

    # step simulation
    simulationstep()

    # check collision with arena walls
    if world.distance(Point(x, y)) < wL / 2:
        break

    if cnt % 50 == 0:
        tfile.write(f'{x}, {y}, {cos(t) * 0.1}, {sin(t) * 0.1}\n')
        pfile.write(f"{x}, {y}, 0.2\n")

end = time.time()
print("Time taken: ", end - start)

tfile.close()
pfile.close()
