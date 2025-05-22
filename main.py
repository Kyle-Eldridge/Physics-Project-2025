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
objects.append(Sphere((0, 0), (7, 0), 1, 1))
objects.append(Sphere((0, -5), (0, 0), 1, 1))
objects.append(StationaryPoint((0, 5)))
objects.append(Bar(objects[0], objects[1], 5))
objects.append(String(objects[0], objects[2], 5))

time.sleep(5)

while True:
    for i in range(updatesPerFrame):
        update()
    draw()
    time.sleep(dt*updatesPerFrame)