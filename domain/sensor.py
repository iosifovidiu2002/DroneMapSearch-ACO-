from .point import Point

class Sensor(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.charge = 0

    def chargeSensor(self):
        self.charge += 1