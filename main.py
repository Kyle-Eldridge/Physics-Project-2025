import math
import matplotlib.pyplot as plt
import numpy as np
import time
from Bar import Bar
from Object import Object
from Sphere import Sphere
from Spring import Spring
from StationaryPoint import StationaryPoint
from String import String
from Surface import Surface
from constants import dt, updatesPerFrame

fig, ax = plt.subplots()
plt.ion()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
objects: list[object] = []

plt.show(block = False)

def update():
    for obj in objects:
        obj.update1(objects)
    for obj in objects:
        obj.update2()

def draw():
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    for obj in objects:
        obj.draw(ax)
    plt.pause(0.01)

# Two spheres bouncing on two surfaces
# objects.append(Sphere((0, 5), (0, 0), 1, 1))
# objects.append(Sphere((0, 0), (1, 0), 1, 1))
# objects.append(Surface((-5, -5), -0.75, 10))
# objects.append(Surface((5, -5), 0.75, 10))

# Two charged conducting spheres on a ramp
# objects.append(StationaryPoint((-9, 8), charge=8e-4))
# objects.append(StationaryPoint((-9, 0), charge=8e-4))
# objects.append(Sphere((-5, 2), (0, 0), 1, 1, bounce=False, charge=2e-3, conduct=True))
# objects.append(Sphere((5, -5), (0, 0), 1, 1, bounce=False, angularVelocity=0, charge=-5e-4, conduct=True))
# objects.append(Surface((0, -5), -0.5, 20, friction=10))
# objects.append(Surface((9, 0), math.pi/2, 20, bounce=True))

# System of spheres attached to a spring
# objects.append(Sphere((5, 0), (0, 0), 1, 1))
# objects.append(Sphere((0, 5), (0, 0), 1, 1))
# objects.append(Surface((0, -9), 0, 20))
# objects.append(Spring(objects[0], objects[1], 2, 30))

# Double pendulum system
# objects.append(Sphere((0, 0), (7, 0), 1, 1))
# objects.append(Sphere((0, -5), (0, 0), 1, 1))
# objects.append(StationaryPoint((0, 5)))
# objects.append(Bar(objects[0], objects[1], 5))
# objects.append(String(objects[0], objects[2], 5))

# Object moving in a circle
# objects.append(Sphere((0, 5), (20, 0), 1, 1, gravity=False))
# objects.append(StationaryPoint((0, 0)))
# objects.append(String(objects[0], objects[1], 5))

# Traingular structure
# objects.append(Sphere((0, 2), (2, 0), 1, 1))
# objects.append(Sphere((-2, 0), (2, 0), 1, 1))
# objects.append(Sphere((2, 0), (2, 0), 1, 1))
# objects.append(Surface((0, -5), 0, 20, friction=0))
# objects.append(Surface((9, 0), math.pi/2, 20, friction=0))
# objects.append(Bar(objects[0], objects[1], 2*math.sqrt(2)))
# objects.append(Bar(objects[0], objects[2], 2*math.sqrt(2)))
# objects.append(Spring(objects[1], objects[2], 4, 300))

import random

# Clear objects list if running interactively
objects.clear()

# Create five spheres hanging from stationary points (like Newton's Cradle)
num_balls = 5
spacing = 2
top_y = 6
ball_radius = 0.5
ball_density = 1
string_length = 6

anchors = []
balls = []

for i in range(num_balls):
    anchor_pos = (-spacing*2 + i*spacing, top_y)
    ball_pos = (anchor_pos[0], top_y - string_length)
    anchor = StationaryPoint(anchor_pos, radius=0.1, color="black")
    ball = Sphere(ball_pos, (random.uniform(-2,2), 0), ball_radius, ball_density, color="blue", gravity=True, bounce=True, friction=0.1)
    objects.append(anchor)
    objects.append(ball)
    anchors.append(anchor)
    balls.append(ball)
    objects.append(String(anchor, ball, string_length, color="black"))

# Add springs between adjacent balls for extra chaos
for i in range(num_balls-1):
    objects.append(Spring(balls[i], balls[i+1], spacing, 10))

# Add a moving platform underneath
platform = Surface((0, -4), 0, 12, friction=0.5, bounce=True)
objects.append(platform)

# Give the first ball a big push
balls[0].velocity = (30, 0)

time.sleep(5)

while True:
    for i in range(updatesPerFrame):
        update()
    draw()
    time.sleep(dt*updatesPerFrame)