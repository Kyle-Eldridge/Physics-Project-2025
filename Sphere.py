import math
import random

from matplotlib.patches import Circle
from Object import Object
from Surface import Surface
import main
import utils

class Sphere(Object):
    def __init__(self, position: tuple[float, float], velocity: tuple[float, float], radius: float, density: float, charge: float = 0, color: str = "gray", gravity: bool = True, bounce: bool = True, angularVelocity: float = 0):
        self.position = position
        self.velocity = velocity
        self.density = density
        self.radius = radius
        self.color = color
        self.charge = charge
        self.mass = (4/3) * math.pi * (radius ** 3) * density
        self.gravity = gravity
        self.bounce = bounce
        self.acceleration = (0, 0)
        self.angularVelocity = angularVelocity
        self.angularAcceleration = 0
        self.inertia = (2/5) * self.mass * (radius ** 2)
        self.shape = Circle(self.position, self.radius, color=self.color)
        self.shape.set_alpha(0.5)
        self.shape.set_zorder(100+random.random())
    
    def update(self, objects: list["Object"]) -> None:
        if self.gravity:
            self.acceleration = (0, -9.8)
        else:
            self.acceleration = (0, 0)
        self.angularAcceleration = 0
        for obj in objects:
            if obj is self:
                continue
            if isinstance(obj, Sphere):
                if utils.sphereSphereCollide(self, obj):
                    self.handleSphereCollision(obj)
            elif isinstance(obj, Surface):
                if utils.sphereSurfaceCollide(self, obj):
                    self.handleSurfaceCollision(obj)
        
        
        # Update position
        self.position = (
            self.position[0] + self.velocity[0]*main.dt + 0.5*self.acceleration[0]*main.dt*main.dt,
            self.position[1] + self.velocity[1]*main.dt + 0.5*self.acceleration[1]*main.dt*main.dt
        )

        # Update velocity
        self.velocity = (
            self.velocity[0] + self.acceleration[0]*main.dt,
            self.velocity[1] + self.acceleration[1]*main.dt
        )

        # Update angular velocity
        self.angularVelocity += self.angularAcceleration * main.dt

        # Update shape position
        self.shape.set_center(self.position)

    def draw(self, ax):
        ax.add_patch(self.shape)

    def handleSurfaceCollision(self, surface: Surface):
        v = utils.rotatePoint(self.velocity, -surface.angle)
        vx, vy = v
        if self.bounce:
            vy *= -1
        else:
            vy = 0
        
        fN = abs(vy-v[1])/main.dt*self.mass
        fF = fN * surface.friction
        