import math
import random

from matplotlib.patches import Circle
from Object import Object
from StationaryPoint import StationaryPoint
from Surface import Surface
from constants import dt
import utils

class Sphere(Object):
    def __init__(self, position: tuple[float, float], velocity: tuple[float, float], radius: float, density: float, charge: float = 0, color: str = "gray", gravity: bool = True, bounce: bool = True, angularVelocity: float = 0, friction: float = 0, conduct: bool = False):
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
        self.friction = friction
        self.inertia = (2/5) * self.mass * (radius ** 2)
        self.shape = Circle(self.position, self.radius, color=self.color)
        self.shape.set_alpha(1)
        self.shape.set_zorder(100+random.random())
        self.conduct = conduct
    
    def update1(self, objects: list["Object"]) -> None:
        if self.gravity:
            self.acceleration = (0, -9.8)
        else:
            self.acceleration = (0, 0)
        self.angularAcceleration = 0
        for obj in objects:
            if obj is self:
                continue
            if isinstance(obj, Sphere):
                r = utils.subPoints(self.position, obj.position)
                # This uses r^3 because I multiply by the position difference r to get the vector
                a = 8.98755e9*self.charge*obj.charge/(utils.magnitude(r)**3)/self.mass
                self.acceleration = utils.addPoints(self.acceleration, utils.mult(r, a))
                if utils.sphereSphereCollide(self, obj):
                    self.handleSphereCollision(obj)
            elif isinstance(obj, Surface):
                if utils.sphereSurfaceCollide(self, obj):
                    self.handleSurfaceCollision(obj)
        
    def update2(self):
        # Update position
        self.position = (
            self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt,
            self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt
        )

        # Update velocity
        self.velocity = (
            self.velocity[0] + self.acceleration[0]*dt,
            self.velocity[1] + self.acceleration[1]*dt
        )

        # Update angular velocity
        self.angularVelocity += self.angularAcceleration * dt

        # Update shape position
        self.shape.set_center(self.position)

    def draw(self, ax):
        ax.add_patch(self.shape)

    def handleSphereCollision(self, sphere: "Sphere"):
        # Calculate the normal vector
        normal = utils.subPoints(self.position, sphere.position)
        normal = utils.normalize(normal)

        self.position = utils.addPoints(sphere.position, utils.mult(normal, self.radius+sphere.radius-0.00001))

        # Calculate the relative velocity
        relativeVelocity = utils.subPoints(self.velocity, sphere.velocity)

        # Calculate the velocity along the normal
        velocityAlongNormal = utils.dot(relativeVelocity, normal)

        perpendicularVelocity = utils.cross(relativeVelocity, normal)

        # If the spheres are moving apart, do nothing
        if velocityAlongNormal > 0:
            return

        # Calculate the restitution coefficient
        e = 1 if self.bounce or sphere.bounce else 0.1

        # Calculate the impulse scalar
        j = -(1+e)*velocityAlongNormal / (1/self.mass + 1/sphere.mass)

        impulse = (j * normal[0], j * normal[1])
        force = utils.div(impulse, dt)
        self.acceleration = utils.addPoints(self.acceleration, utils.div(force, self.mass))

        friction = utils.magnitude(force) * (self.friction+sphere.friction) / 2
        relativeAngularVelocity = self.angularVelocity + sphere.angularVelocity*sphere.radius/self.radius + perpendicularVelocity/self.radius
        frictionVector = utils.mult(utils.rotatePoint(normal, math.pi/2), 
                                        min(friction, abs(relativeAngularVelocity/dt*self.inertia/self.radius)) * utils.sign(relativeAngularVelocity))
        self.acceleration = utils.addPoints(self.acceleration, utils.div(frictionVector, self.mass))
        self.angularAcceleration -= min(friction * self.radius / self.inertia, abs(relativeAngularVelocity) / dt) * utils.sign(relativeAngularVelocity)

        if self.conduct and sphere.conduct:
            # q1/r1=q2/r2
            # q1 = (qTotal-q1)r1/r2
            # q1(1+r1/r2)=qTotal*r1/r2
            qTotal = self.charge + sphere.charge
            self.charge = qTotal*self.radius/sphere.radius/(1+self.radius/sphere.radius)
            sphere.charge = qTotal - self.charge


    def handleSurfaceCollision(self, surface: Surface):
        p = utils.rotatePoint(utils.subPoints(self.position, surface.position), -surface.angle)
        nearest = (utils.clamp(p[0], -surface.size/2, surface.size/2), utils.clamp(p[1], -surface.thickness/2, surface.thickness/2))
        nearest = utils.addPoints(surface.position, utils.rotatePoint(nearest, surface.angle))
        tempPoint = StationaryPoint(nearest, 0, bounce = surface.bounce, friction = surface.friction)
        self.handleSphereCollision(tempPoint)
        
