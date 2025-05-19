import matplotlib.pyplot as plt
import numpy as np
import time
from Object import Object

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
objects: list[object] = []

def update():
    for obj in objects:
        obj.update(objects)

def draw():
    ax.clear()
    for obj in objects:
        obj.draw(ax)
    plt.pause(0.01)
