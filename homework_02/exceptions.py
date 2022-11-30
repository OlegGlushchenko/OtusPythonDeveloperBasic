"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class BaseError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class LowFuelError(BaseError):
    pass


class NotEnoughFuel(BaseError):
    pass


class CargoOverload(BaseError):
    pass


