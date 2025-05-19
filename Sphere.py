from Object import Object

class Sphere(Object):
    def __init__(self, position: tuple[float, float, float], velocity: tuple[float, float, float], radius: float, density: float, charge: float = 0, color: str = "gray", gravity: bool = True, bounce: bool = True, elastic: float = 0.5, angularVelocity: tuple[float, float, float] = (0, 0, 0)):
        self.position = position
        self.velocity = velocity
        self.density = density
        self.radius = radius
        self.color = color
        self.charge = charge
        self.mass = (4/3) * 3.14159 * (radius ** 3) * density
        self.gravity = gravity
        self.bounce = bounce
        self.elastic = elastic
        self.acceleration = (0, 0, 0)
        self.angularVelocity = angularVelocity
        self.angularAcceleration = (0, 0, 0)
        self.inertia = (2/5) * self.mass * (radius ** 2)
    
    def update(self, objects: list["Object"]) -> None:
        if self.gravity:
            self.acceleration = (0, -9.81, 0)
        else:
            self.acceleration = (0, 0, 0)
        
        # Update velocity
        self.velocity = (
            self.velocity[0] + self.acceleration[0],
            self.velocity[1] + self.acceleration[1],
            self.velocity[2] + self.acceleration[2]
        )
        
        # Update position
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2]
        )