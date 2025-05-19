import math
from Object import Object
import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import Polygon

class Surface(object):
    def __init__(self, position: tuple[float, float, float], angle: tuple[float, float], size: tuple[float, float], friction: float = 0.5, color: str = "gray"):
        self.position = position
        self.angle = angle
        self.size = size
        self.friction = friction
        self.color = color
        self.thickness = 0.1
                
        # Precompute the 3D corners of the rectangle centered at (0,0,0)
        w, h = size
        corners = np.array([
            [-w/2, -h/2, 0],
            [ w/2, -h/2, 0],
            [ w/2,  h/2, 0],
            [-w/2,  h/2, 0]
        ])

        # Convert angles to radians
        theta_z, theta_x = angle

        # Rotation matrix about z-axis
        Rz = np.array([
            [np.cos(theta_z), -np.sin(theta_z), 0],
            [np.sin(theta_z),  np.cos(theta_z), 0],
            [0, 0, 1]
        ])
        # Rotation matrix about x-axis
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(theta_x), -np.sin(theta_x)],
            [0, np.sin(theta_x),  np.cos(theta_x)]
        ])

        # Apply rotations: first z, then x
        rotated = corners @ Rz.T @ Rx.T

        # Translate to position
        rotated += np.array(position)
        self.corners = rotated

        projected_2d = rotated[:, :2]
        self.shape = Polygon(projected_2d, closed=True, color=color, alpha=0.5)
        self.shape.set_edgecolor("black")

    def update(self, objects: list["Object"]) -> None:
        pass

    def draw(self, ax) -> None:
        ax.add_patch(self.shape)
