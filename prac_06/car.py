class Car:
    """Represent a Car object."""
    def __init__(self, fuel=0, name="Car"):

        self.fuel = fuel
        self._odometer = 0
        self.name = name

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return string representation of Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
