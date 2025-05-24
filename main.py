import math
import matplotlib.pyplot as plt
import numpy as np
import time
from Bar import Bar
from MagneticFieldCircle import MagneticFieldCircle
from MagneticFieldRect import MagneticFieldRect
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
    ax.set_axis_off()
    for obj in objects:
        obj.draw(ax)
    plt.pause(0.001)

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
# objects.append(Sphere((0, 0), (7, 0), 1, 1, charge=1e-4))
# objects.append(Sphere((0, -5), (0, 0), 1, 1, charge=1e-4))
# objects.append(StationaryPoint((0, 5)))
# objects.append(Spring(objects[0], objects[1], 5, 100))
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

# Charged object moving into a magnetic field
# objects.append(Sphere((0, 0), (5, 0), 0.5, 1/50**3, gravity=False, charge = 1e-6))
# objects.append(MagneticFieldRect((7, 0), 10, 20, 10))
# objects.append(MagneticFieldRect((-7, 0), 10, 20, 10))

# Example for presentation
# Double pendulum
objects.append(StationaryPoint((-5, 9.5), radius=0.2))
objects.append(Sphere((-5, 6.5), (0, 0), 0.5, 1, 7e-6))
objects.append(Sphere((-5, 3.5), (0, 0), 0.5, 1, 0))
objects.append(Surface((-9.9, 0), math.pi/2, 20, 0, surfaceChargeDensity=-1e-5, bounce=True))
objects.append(Surface((-0.1, 5), math.pi/2, 10, 0, surfaceChargeDensity=1e-5, bounce=True))
objects.append(String(objects[0], objects[1], 3))
objects.append(Bar(objects[1], objects[2], 3, lineWidth=5))
# Falling non-ideal spring system
objects.append(Sphere((3, 5), (0, 0), 1, 1, 1e-9, friction=1, bounce=True))
objects.append(Sphere((9, 5), (0, 4), 1, 1, 1e-9, friction=1, bounce=False))
objects.append(Spring(objects[7], objects[8], 4, lambda x: -30*x*abs(x)))
# Ramp and magnetic field
objects.append(Surface((0, -6), 0.4, 30, 1))
objects.append(MagneticFieldRect((-7, -5.5), 8, 8, 1e10, 0.4))

time.sleep(5)

while True:
    t1 = time.time_ns()
    for i in range(updatesPerFrame):
        update()
    draw()
    t2 = time.time_ns()
    t = (t2-t1)/1e9
    time.sleep(max(dt*updatesPerFrame - t, 0))