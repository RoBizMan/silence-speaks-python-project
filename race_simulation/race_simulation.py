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


def simulate_race():
    """
    Simulate a race between a motorcycle, a car, and a truck,
    and determine the winner.

    Returns:
        tuple: A tuple containing the name of the winning vehicle and
        a dictionary of race times for each vehicle.
    """
    motorcycle = Motorcycle("Royal Enfield")
    car = Car("Hindustan Ambassador")
    truck = Truck("Tata 1210")

    vehicles = [motorcycle, car, truck]

    times = {vehicle.name: vehicle.race_track() for vehicle in vehicles}
    winner = min(times, key=times.get)

    # Format times for better display
    formatted_times = {name:
                    format_time(time) for name, time in times.items()}
    
    return winner, formatted_times


def format_time(seconds):
    """
Convert time in seconds to a formatted string of minutes and seconds.
    """
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes}m {remaining_seconds:.2f}s"


def main():
    while True:
        user_input = input(
            "\nPress Enter to start the simulation or type 'quit' to exit: "
        ).strip().lower()

        if user_input == 'quit':
            print("\nExiting the race simulation. Goodbye!\n")
            break

        if user_input:
            print(
                "\nInvalid input! Please press Enter to start the simulation"
                " or type 'exit' to quit."
            )
            continue

        while True:
            try:
                number_races = int(
                    input("\nEnter the number of races to simulate: ")
                )
                for i in range(number_races):
                    winner, times = simulate_race()
                    print(
                        f"Race {i + 1}: Winner is {winner} "
                        f"with times: {times}\n"
                    )
            except ValueError:
                print("Please enter a valid number for the number of races.")
                continue

            end_race_input = input(
                "Simulation complete. Type 'restart' to simulate again "
                "or 'exit' to quit: "
            ).strip().lower()

            if end_race_input == "exit":
                print("\nExiting the race simulation. Goodbye!\n")
                exit()
            elif end_race_input == "restart":
                print("\nRestarting the simulation...")
                break
            else:
                print(
                    "Invalid input! Please type 'restart' to simulate again "
                    "or 'exit' to quit: "
                )

if __name__ == "__main__":
    main()
