import matplotlib.pyplot as plt
import numpy as np
import time
from Object import Object
from Sphere import Sphere
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

objects.append(Sphere((0, 5), (0, 0), 1, 1))
objects.append(Sphere((0, 0), (0, 0), 1, 1, gravity=False))
objects.append(Surface((0, -5), 0.2, 10))

time.sleep(5)

while True:
    update()
    draw()
    time.sleep(dt)