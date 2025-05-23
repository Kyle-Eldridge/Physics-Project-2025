from matplotlib.patches import Circle
from Object import Object

import utils


class MagneticFieldCircle(object):
    # + field is out of the page
    def __init__(self, position: tuple[float, float], radius: float, fieldStrength: float, color: str = "gray", alpha: float = 0.5):
        self.position = position
        self.radius = radius
        self.fieldStrength = fieldStrength
        self.color = color
        self.alpha = alpha
        self.shape = Circle(self.position, self.radius, color=self.color)
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
        return utils.sphereSphereCollide(self, obj)