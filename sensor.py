class Sensor:
    def __init__(self, pressure=19):
        self.pressure = pressure

    def sample_pressure(self):
        return self.pressure
