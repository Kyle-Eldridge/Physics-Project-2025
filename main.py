import math
import matplotlib.pyplot as plt
import numpy as np
import time
from Object import Object
from Sphere import Sphere
from StationaryPoint import StationaryPoint
from Surface import Surface
from constants import dt

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

# objects.append(Sphere((0, 5), (0, 0), 1, 1))
# objects.append(Sphere((0, 0), (1, 0), 1, 1))
# objects.append(Surface((-5, -5), -0.75, 10))
# objects.append(Surface((5, -5), 0.75, 10))

objects.append(StationaryPoint((-9, 8), charge=8e-4))
objects.append(StationaryPoint((-9, 0), charge=8e-4))
objects.append(Sphere((-5, 2), (0, 0), 1, 1, bounce=False, charge=2e-3, conduct=True))
objects.append(Sphere((5, -5), (0, 0), 1, 1, bounce=False, angularVelocity=0, charge=-5e-4, conduct=True))
objects.append(Surface((0, -5), -0.5, 20, friction=10))
objects.append(Surface((9, 0), math.pi/2, 20, bounce=True))

time.sleep(5)

while True:
    update()
    draw()
    time.sleep(dt)