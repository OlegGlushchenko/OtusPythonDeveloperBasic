from homework_02.base import Vehicle
from engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    engine = None

    def set_engine(self, import_engine: Engine):
        self.engine = import_engine
