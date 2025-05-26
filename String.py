from Object import Object
from Sphere import Sphere
import utils
from constants import dt

class String(Object):
    def __init__(self, object1: Sphere, object2: Sphere, length: float, color: str = "black"):
        self.object1 = object1
        self.object2 = object2
        self.length = length
        self.color = color

    def update1(self, objects):
        length = utils.dist(self.object1.position, self.object2.position)
        if length > self.length:
            direction = utils.normalize(utils.subPoints(self.object1.position, self.object2.position))
            relativeVelocity = utils.subPoints(self.object1.velocity, self.object2.velocity)
            velocityAlongString = utils.dot(relativeVelocity, direction)
            if velocityAlongString > 0:
                J = velocityAlongString / (1/self.object1.mass + 1/self.object2.mass)
                self.object1.acceleration = utils.addPoints(self.object1.acceleration, utils.mult(direction, -J/self.object1.mass/dt))
                self.object2.acceleration = utils.addPoints(self.object2.acceleration, utils.mult(direction, J/self.object2.mass/dt))
        
    def update2(self):
        # Project positions to enforce the string length constraint
        delta = utils.subPoints(self.object1.position, self.object2.position)
        dist = utils.magnitude(delta)
        if dist == 0 or dist < self.length:
            return
        totalMass = self.object1.mass + self.object2.mass
        correction1 = utils.mult(delta, (dist - self.length) / dist * self.object2.mass / totalMass)
        correction2 = utils.mult(delta, (dist - self.length) / dist * self.object1.mass / totalMass)
        self.object1.position = utils.subPoints(self.object1.position, correction1)
        self.object2.position = utils.addPoints(self.object2.position, correction2)

    def draw(self, ax):
        p1 = self.object1.position
        p2 = self.object2.position

        # Draw a line between the two spheres
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=self.color, linewidth=2)