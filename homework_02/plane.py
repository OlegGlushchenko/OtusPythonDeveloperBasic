from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def load_cargo(self, cargo_for_loading):
        if (self.cargo + cargo_for_loading) > self.max_cargo:
            raise CargoOverload("Overload")
        self.cargo = self.cargo + cargo_for_loading

    def remove_all_cargo(self):
        cargo_before_clearing = self.cargo
        self.cargo = 0
        return cargo_before_clearing
