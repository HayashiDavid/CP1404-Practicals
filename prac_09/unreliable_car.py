import random
from prac_09.car import Car

LOW_RANDOM_NUMBER = 0
HIGH_RANDOM_NUMBER = 100


class UnreliableCar(Car):
    """An unreliable version of car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

