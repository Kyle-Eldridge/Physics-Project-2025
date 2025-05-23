import math
from Object import Object
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle

import utils

class Surface(object):
    def __init__(self, position: tuple[float, float], angle: float, size: float, friction: float = 0.5, color: str = "black", bounce: bool = False, thickness: float = 0.1, surfaceChargeDensity: float = 0):
        self.position = position
        self.angle = angle
        self.size = size
        self.friction = friction
        self.color = color
        self.thickness = thickness
        self.bounce = bounce
        self.chargeDensity = surfaceChargeDensity
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

    def getEField(self, point: tuple[float, float]) -> tuple[float, float]:
        # Calculate the electric field at the given point
        E = (0, 0)
        if self.chargeDensity != 0:
            n = 50
            dx = self.size/n
            for i in range(n):
                x = i * dx - self.size/2
                p = utils.addPoints(self.position, (x * math.cos(self.angle), x * math.sin(self.angle)))
                r = utils.subPoints(point, p)
                r_magnitude = utils.magnitude(r)
                if r_magnitude != 0:
                    E2 = 2 * 8.98755e9 * self.chargeDensity*dx / r_magnitude
                    E = utils.addPoints(E, utils.mult(r, E2/r_magnitude))
        return E