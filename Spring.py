import math
import numpy as np
from Object import Object
from Sphere import Sphere
import utils
from typing import Callable

class Spring(Object):
    def __init__(self, object1: Sphere, object2: Sphere, restLength: float, springConstant: float | Callable[[float], float], color: str = "black"):
        self.object1 = object1
        self.object2 = object2
        self.restLength = restLength
        self.color = color
        if isinstance(springConstant, (int, float)):
            self.forceEquation = lambda x: -springConstant * x
        else:
            self.forceEquation = springConstant

    def update1(self, objects):
        length = utils.dist(self.object1.position, self.object2.position)
        force = self.forceEquation(length - self.restLength)
        direction = utils.normalize(utils.subPoints(self.object1.position, self.object2.position))
        self.object1.acceleration = utils.addPoints(self.object1.acceleration, utils.mult(direction, force/self.object1.mass))
        self.object2.acceleration = utils.addPoints(self.object2.acceleration, utils.mult(direction, -force/self.object2.mass))
    
    def update2(self):
        pass

    # This method was written by AI because I don't know how to draw a spring
    def draw(self, ax):
        # Parameters for spring appearance
        num_coils = math.ceil(5*self.restLength)  # Number of coils in the spring
        amplitude = 0.2  # How "wide" the spring wiggles

        p1 = self.object1.position
        p2 = self.object2.position

        # Vector from p1 to p2
        v = utils.subPoints(p2, p1)
        length = utils.magnitude(v)
        angle = utils.angle(v)

        # Generate points along the spring
        t = np.linspace(0, 1, num_coils * 2 + 1)
        # Spring wiggle in local coordinates
        x = t * length
        y = amplitude * np.sin(t * num_coils * np.pi)

        # Rotate and translate points to world coordinates
        coords = np.vstack((x, y))
        rotation = np.array([[np.cos(angle), -np.sin(angle)],
                            [np.sin(angle),  np.cos(angle)]])
        coords = rotation @ coords
        coords[0] += p1[0]
        coords[1] += p1[1]

        ax.plot(coords[0], coords[1], color=self.color, linewidth=2)