from matplotlib.axes import Axes


class Object:
    def __init__(self):
        pass
    def update1(self, objects: list["Object"]) -> None:
        pass
    def update2(self) -> None:
        pass
    def draw(self, ax: Axes) -> None:
        pass