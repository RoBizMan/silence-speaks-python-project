from collections import defaultdict


def load_city_node(file_path):
    """
    Extract pairs of connected cities nodes from the file
    and create a graph representation.

    Args:
        file_path (str): The path to the file containing city connections.

    Returns:
        dict: A dictionary representing the graph of connected cities.
    """
    graph = defaultdict(list)
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    city1, city2 = map(str.strip, line.split(','))
                except ValueError:
                    raise ValueError(
                        f"Error: Line '{line}' is not properly formatted. "
                        "Expected format: 'City1, City2'."
                    )
                if city1 == city2:
                    print(
                        f"Warning: Ignoring self-loop for city '{city1}'. "
                        f"A city node cannot connect to itself."
                    )
                    continue
                graph[city1].append(city2)
                graph[city2].append(city1)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"The file '{file_path}' was not found."
        ) from e
    except IOError as e:
        raise IOError(
            f"An error occurred while reading the file '{file_path}'."
        ) from e
    return graph


def check_connected_cities(graph, city1, city2):
    """
    Checks if two cities are connected in the graph using
    Depth-First Search (DFS).

    This function determines whether there is a path of connected cities
    between `city1` and `city2` by traversing the graph. It returns `True`
    if a path exists, otherwise it returns `False`. The graph is represented
    as an adjacency list, where each city points to a list of cities
    it is connected to.

    Args:
        graph (dict): A dictionary representing the graph of connected cities,
                    where keys are city names and values are lists of cities
                    directly connected to the key city.
        city1 (str): The name of the first city to check for connectivity.
        city2 (str): The name of the second city to check for connectivity.

    Returns:
        bool: `True` if there is a path between `city1` and `city2`,
            `False` otherwise.
    """
    if city1 not in graph or city2 not in graph:
        return False

    visited = set()

    def dfs(current_city):
        if current_city == city2:
            return True
        visited.add(current_city)
        for related_city in graph[current_city]:
            if related_city not in visited:
                if dfs(related_city):
                    return True
        return False

    return dfs(city1)


def main():
    """
    Main function to load city connections and interact with the user to check
    if two cities are connected. The user can input two city names, and the
    function will determine if the cities are connected either directly or
    indirectly through other cities. The program handles various input
    validations, including checking for valid city names, ensuring that cities
    do not contain numbers, and preventing the user from entering the same
    city twice.

    The user can exit the program by typing 'exit' at any prompt.

    The graph of connected cities is loaded from a file and stored as an
    adjacency list where each city is associated with a list of directly
    connected cities.

    The program will handle the following scenarios:
        - Invalid city name (empty or containing numbers).
        - Cities that do not exist in the graph.
        - Cities that are already the same.
        - Inform the user if two cities are connected or not.

    This function runs in an infinite loop until the user opts to exit.

    Raises:
        Exception: Any error encountered during the file loading or city
        connection checks.
    """
    file_path = 'connected_cities/cities_nodes.txt'
    try:
        city_graph = load_city_node(file_path)
        print("Graph loaded successfully.")

        while True:
            city1 = input(
                "Enter the first city (or type 'exit' to quit): "
            ).strip()

            if city1.lower() == 'exit':
                print("Exiting program.")
                break

            if not city1:
                print("error: Please enter a valid city name.")
                continue

            if any(char.isdigit() for char in city1):
                print("Error: City name cannot contain numbers.")
                continue

            city2 = input(
                "Enter the second city (or type 'exit' to quit): "
            ).strip()

            if city2.lower() == 'exit':
                print("Exiting program.")
                break

            if not city2:
                print("error: Please enter a valid city name.")
                continue

            if any(char.isdigit() for char in city2):
                print("Error: City name cannot contain numbers.")
                continue

            formatted_city1 = city1.capitalize()
            formatted_city2 = city2.capitalize()

            # Error handling for same city input
            if formatted_city1 == formatted_city2:
                print("Error: You entered the same city for both inputs.")
                continue

            # Error handling for non-existent cities
            if (
                formatted_city1 not in city_graph
                    or formatted_city2 not in city_graph):
                print(
                    f"Error: One or both of the cities '{formatted_city1}'"
                    f" and '{formatted_city2}' do not exist.")
                continue

            # Check connectivity
            if check_connected_cities(
                city_graph, formatted_city1, formatted_city2
            ):
                print(
                    f"{formatted_city1} and {formatted_city2} are connected."
                )
            else:
                print(
                    f"{formatted_city1} and {formatted_city2} are "
                    "NOT connected."
                )

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
