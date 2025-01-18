import random

class Vehicle:
    """
    Base class for all vehicles in the race simulation.

    Attributes:
        name (str): The name of the vehicle.
        speed (float): The maximum speed of the vehicle in
            kilometers per hour (km/h).
        acceleration (float): The acceleration of the vehicle in
            meters per second squared (m/s^2).
        gross_weight (float): The gross weight of the vehicle in
            kilograms (kg).

    Methods:
        race(): Simulates a race for this vehicle and calculates the time
            taken to finish a fixed distance.
    """
    def __init__(self, name, speed, acceleration, weight):
        self.name = name
        # Speed in km/h
        self.speed = speed
        # Acceleration in m/s^2
        self.acceleration = acceleration
        # Vehicle gross weight in kg
        self.weight = weight

    def race_track(self):
        # Distance in meters
        distance = 2000
        # Adjust realistic speed influenced by vehicle gross weight
        realistic_speed = self.speed * (1 - (self.weight / 10000))
        # Convert speed from km/h to m/s
        time = distance / (realistic_speed / 3.6)
        return time


class Motorcycle(Vehicle):
    """
    Represents a motorcycle in the race simulation.

    Inherits from the Vehicle class and initialises with
        random speed, acceleration, and gross weight.

    Attributes:
        name (str): The name of the motorcycle.
        speed (float): Randomly assigned speed between 70 and 100 km/h.
        acceleration (float): Randomly assigned acceleration
            between 6 and 10 m/s^2.
        gross_weight (float): Randomly assigned weight
            between 200 and 400 kg.
    """
    def __init__(self, name):
        super().__init__(
            name,
            speed=random.randint(70, 100),
            acceleration=random.uniform(6, 10),
            weight=random.randint(200, 400)
        )


class Car(Vehicle):
    """
    Represents a car in the race simulation.

    Inherits from the Vehicle class and initialises with
        random speed, acceleration, and gross weight.

    Attributes:
        name (str): The name of the car.
        speed (float): Randomly assigned speed between 90 and 130 km/h.
        acceleration (float): Randomly assigned acceleration
            between 4 and 6 m/s^2.
        gross_weight (float): Randomly assigned weight
            between 1800 and 3250 kg.
    """
    def __init__(self, name):
        super().__init__(
            name,
            speed=random.randint(90, 130),
            acceleration=random.uniform(4, 6),
            weight=random.randint(1800, 3250)
        )


class Truck(Vehicle):
    """
    Represents a truck in the race simulation.

    Inherits from the Vehicle class and initialises with
        random speed, acceleration, and gross weight.

    Attributes:
        name (str): The name of the truck.
        speed (float): Randomly assigned speed between 60 and 100 km/h.
        acceleration (float): Randomly assigned acceleration
            between 2 and 4 m/s^2.
        gross_weight (float): Randomly assigned weight
            between 4225 and 9375 kg.
    """
    def __init__(self, name):
        super().__init__(
            name,
            speed=random.randint(60, 100),
            acceleration=random.uniform(2, 4),
            weight=random.randint(4225, 9375)
        )

