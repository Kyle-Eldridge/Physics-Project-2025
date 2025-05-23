import math
from matplotlib.patches import Rectangle
from Object import Object

import utils


class MagneticFieldRect(object):
    # + field is out of the page
    def __init__(self, position: tuple[float, float], width: float, height: float, fieldStrength: float, angle: float = 0, color: str = "gray", alpha: float = 0.5):
        self.position = position
        self.fieldStrength = fieldStrength
        self.color = color
        self.width = width
        self.height = height
        self.angle = angle
        self.alpha = alpha
        self.shape = Rectangle(
            (self.position[0] - self.width / 2 * math.cos(angle) + self.height / 2 * math.sin(angle),
             self.position[1] - self.width / 2 * math.sin(angle) - self.height / 2 * math.cos(angle)),
            self.width, self.height, angle=self.angle*180/math.pi, color=self.color)
        self.shape.set_alpha(self.alpha)
        self.shape.set_zorder(200)
        self.shape.set_linewidth(0)
    
    def update1(self, objects):
        pass
    def update2(self):
        pass
    def draw(self, ax):
        ax.add_patch(self.shape)

    def collide(self, obj):
        return utils.sphereRectCollide(obj, self)