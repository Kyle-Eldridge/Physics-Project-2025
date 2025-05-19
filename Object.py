from matplotlib.axes import Axes


class Object:
    def __init__(self):
        pass
    def update(self, objects: list["Object"]) -> None:
        pass
    def draw(self, ax: Axes) -> None:
        pass