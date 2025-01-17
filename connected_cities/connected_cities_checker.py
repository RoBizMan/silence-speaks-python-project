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
                # Remove empty line and verify that the line is not empty
                line = line.strip()
                if not line:
                    continue
                try:
                    # Handle incorrect formatting
                    city1, city2 = map(str.strip, line.split(','))
                # Raise the error if connected cities nodes in the file is not
                # formatted properly
                except ValueError:
                    raise ValueError(
                        f"Error: Line '{line}' is not properly formatted. "
                        "Expected format: 'City1, City2'."
                    )
                # Prevents the city node from self-loop
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


if __name__ == "__main__":
    file_path = 'connected_cities/cities_nodes.txt'
    try:
        city_graph = load_city_node(file_path)
        print("Graph loaded successfully.")
        print(city_graph)
    except ValueError as e:
        print(e)