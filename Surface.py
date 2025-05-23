import math
from Object import Object
import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle

class Surface(object):
    def __init__(self, position: tuple[float, float], angle: float, size: float, friction: float = 0.5, color: str = "black", bounce: bool = False):
        self.position = position
        self.angle = angle
        self.size = size
        self.friction = friction
        self.color = color
        self.thickness = 0.1
        self.bounce = bounce
        self.shape = Rectangle(
            (self.position[0] - self.size / 2 * math.cos(angle) + self.thickness / 2 * math.sin(angle),
             self.position[1] - self.size / 2 * math.sin(angle) - self.thickness / 2 * math.cos(angle)),
            self.size, self.thickness, angle=self.angle*180/math.pi, color=self.color)
        self.shape.set_linewidth(0)
        self.shape.set_zorder(0)

    def update1(self, objects: list[Object]) -> None:
        pass
    def update2(self) -> None:
        pass

    def draw(self, ax) -> None:
        ax.add_patch(self.shape)
