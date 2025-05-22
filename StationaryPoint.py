from Sphere import Sphere

class StationaryPoint(Sphere):
    def __init__(self, position: tuple[float, float], radius: float = 0.1, charge: float = 0, color: str = "black", bounce: bool = True, friction: float = 0, conduct: bool = False):
        super().__init__(position, (0, 0), radius, 0, charge, color, False, bounce, 0, friction, conduct)
        self.mass = 1e1000
        self.inertia = 1e1000