from examples.utils import Container


class Engine:
    def __init__(self, model):
        self.model = model


class Passenger:

    def __init__(self, name):
        self.name = name


class Passengers(Container):
    pass


class Car:

    def __init__(self, engine, passengers):
        self.engine = engine
        self.passengers = Passengers(passengers)
