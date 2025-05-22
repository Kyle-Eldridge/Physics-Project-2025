from Object import Object
from Sphere import Sphere
from String import String
import utils
from constants import dt

class Bar(String):
    def __init__(self, object1: Sphere, object2: Sphere, length: float, color: str = "gray"):
        super().__init__(object1, object2, length, color)

    def update1(self, objects):
        length = utils.dist(self.object1.position, self.object2.position)
        direction = utils.normalize(utils.subPoints(self.object1.position, self.object2.position))
        relativeVelocity = utils.subPoints(self.object1.velocity, self.object2.velocity)
        velocityAlongString = utils.dot(relativeVelocity, direction)+(length-self.length)*5
        J = velocityAlongString / (1/self.object1.mass + 1/self.object2.mass)
        self.object1.acceleration = utils.addPoints(self.object1.acceleration, utils.mult(direction, -J/self.object1.mass/dt))
        self.object2.acceleration = utils.addPoints(self.object2.acceleration, utils.mult(direction, J/self.object2.mass/dt))
        
    def draw(self, ax):
        p1 = self.object1.position
        p2 = self.object2.position

        # Draw a line between the two spheres
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=self.color, linewidth=8)