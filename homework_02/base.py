from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=100, fuel=40, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            try:
                if not (self.fuel > 0):
                    raise LowFuelError("Low fuel")
                self.started = not self.started
            except LowFuelError as error:
                print(error.value)
                raise

    def move(self, distance):
        remaining_fuel = self.fuel - distance * self.fuel_consumption
        try:
            if not (remaining_fuel >= 0):
                raise NotEnoughFuel("Not enought fuel")
        except NotEnoughFuel as error:
            print(error.value)
            raise
        self.fuel = remaining_fuel
