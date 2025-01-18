# Silence Speaks Python Project

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project)

---

This repository contains my solutions to the Python coding project provided by Silence Speaks.

---

## Table of Contents
- [Running the Programs](#running-the-programs)
- [Connected Cities Checker](#connected-cities-checker)
- [Simple Race Simulation](#simple-race-simulation)
- [REST API](#rest-api)
- [Testing](#testing)
- [Agile Development Process](#agile-development-process)
- [GitHub Issues](#github-issues)
- [Credits](#credits)

---

## Running the Programs

This project can be cloned or forked in order to make a local copy on your own system. Ensure you have Python installed on your machine.

### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/RoBizMan/silence-speaks-python-project) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/RoBizMan/silence-speaks-python-project.git`
7. Press Enter to create your local clone.

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/RoBizMan/silence-speaks-python-project)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

---

## Connected Cities Checker
This program checks if two cities nodes are connected based on provided connections in a text file.

### Instructions

1. Prepare a `cities_nodes.txt` file with city pairs inside the `connected_cities` folder.

Sample `cities_nodes.txt` file:

```
Vellore, Shillong
Vadodara, Thiruvananthapuram
```

2. Run the program: `python3 connected_cities/connected_cities_checker.py`

3. Input two city names when prompted.

### Example Usage

#### If two cities nodes are connected with edges:

```
Graph loaded successfully
Enter the first city (or type 'exit' to quit): Delhi
Enter the second city (or type 'exit' to quit): Kolkata
Delhi and Kolkata are connected.
```

#### If two cities nodes are not connected with edges:

```
Graph loaded successfully
Enter the first city (or type 'exit' to quit): Guwahati
Enter the second city (or type 'exit' to quit): Delhi
Guwahati and Delhi are NOT connected.
```

---

## Simple Race Simulation
This program simulates races between different vehicles to determine which one wins the race.

### Instructions

1. Run the program: `python3 race_simulation/race_simulation.py`

2. Input the number of races to simulate, with the minimum of 1 and the maximum of 50.

3. Type 'restart' to restart the simulation or 'exit' to quit the simulation.

*Optional: It is possible to modify the vehicle's characteristics in the `race_simulation.py` file.*

*Sample `class Motorcycle(Vehicle):` code snippet:*

```
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
```

### Example Usage

#### Run the simulation and exit the simulation

```
Press Enter to start the simulation or type 'quit' to exit: 

Enter the number of races to simulate (minimum - 1 to maximum - 50): 2
Race 1: Winner is Royal Enfield with times: {'Royal Enfield': '1m 26.13s', 'Hindustan Ambassador': '1m 37.07s', 'Tata 1210': '5m 37.38s'}

Race 2: Winner is Royal Enfield with times: {'Royal Enfield': '1m 25.51s', 'Hindustan Ambassador': '1m 33.55s', 'Tata 1210': '7m 4.78s'}

Simulation complete. Type 'restart' to simulate again or 'exit' to quit: exit

Exiting the race simulation. Goodbye!
```

#### Run the simulation and restart the simulation

The simulation can be restarted as much as a user want to try until they type 'exit' to end the simulation.

```
Press Enter to start the simulation or type 'quit' to exit: 

Enter the number of races to simulate (minimum - 1 to maximum - 50): 2
Race 1: Winner is Hindustan Ambassador with times: {'Royal Enfield': '1m 34.62s', 'Hindustan Ambassador': '1m 26.33s', 'Tata 1210': '4m 51.26s'}

Race 2: Winner is Royal Enfield with times: {'Royal Enfield': '1m 29.04s', 'Hindustan Ambassador': '1m 41.72s', 'Tata 1210': '2m 23.79s'}

Simulation complete. Type 'restart' to simulate again or 'exit' to quit: restart

Restarting the simulation...

Press Enter to start the simulation or type 'quit' to exit:  

Enter the number of races to simulate (minimum - 1 to maximum - 50): 3
Race 1: Winner is Hindustan Ambassador with times: {'Royal Enfield': '1m 38.43s', 'Hindustan Ambassador': '1m 15.26s', 'Tata 1210': '3m 12.60s'}

Race 2: Winner is Royal Enfield with times: {'Royal Enfield': '1m 34.81s', 'Hindustan Ambassador': '1m 35.71s', 'Tata 1210': '4m 16.53s'}

Race 3: Winner is Hindustan Ambassador with times: {'Royal Enfield': '1m 46.15s', 'Hindustan Ambassador': '1m 34.27s', 'Tata 1210': '6m 49.89s'}

Simulation complete. Type 'restart' to simulate again or 'exit' to quit: exit

Exiting the race simulation. Goodbye!
```

---

## REST API

This microservice echoes messages received via HTTP POST and GET requests, including a timestamp in the response. Flask is the chosen framework for this project as it is a lightweight framework and scalability.

### Instructions

1. Create a virtual environment by typing `python3 -m venv venv` in the terminal.

2. Activate a virtual environment by typing in the terminal:
- On macOS/Linux: `source venv/bin/activate`
- On Windows: `.\venv\Scripts\activate`

3. Install the required packages by typing `pip3 install -r rest_microservice/requirements.txt` in the terminal.

*Choose one of the following two options:*

**Option 1**

1. Install [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension from the Visual Studio marketplace.

2. Create a file ends with .http within the REST API folder.

Sample `api_test.http` file:

```
# GET request
GET http://127.0.0.1:5000/echo

###

# POST request
POST http://127.0.0.1:5000/echo
Content-Type: application/json

{
    "message": "Hello, World!"
}
```

3. A "Send Request" button will display above the GET request hyperlink and the POST request hyperlink.

4. Click "Send Request" button and it will display a new split editor with the details of the request.

***or***

**Option 2**

1. Run the program: `python3 rest_microservice/tests/test_routes.py`

2. Open the new bash terminal.

3. To send a GET request, type `curl http://127.0.0.1:5000/echo` in the terminal and it will return the request with message and timestamp.

4. To send a POST request, type `curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{"message": "Hello, World!"}'` in the terminal and it will return the request with message and timestamp.

### Example Usage

#### Send a GET request

##### Via REST Client

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.13.1
Date: Sat, 18 Jan 2025 18:12:13 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "message": "Send a POST request with a message.",
  "timestamp": "2025-01-18T18:12:13.777636+00:00"
}
```

##### Via terminal

```
(venv) host32:silence-speaks-python-project XXXXX$ curl http://127.0.0.1:5000/echo
{"message":"Send a POST request with a message.","timestamp":"2025-01-18T18:11:33.525735+00:00"}
```

#### Send a POST request

##### Via REST Client

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.13.1
Date: Sat, 18 Jan 2025 18:14:27 GMT
Content-Type: application/json
Content-Length: 75
Connection: close

{
  "message": "Hello, World!",
  "timestamp": "2025-01-18T18:14:27.923479+00:00"
}
```

##### Via terminal

```
(venv) host32:silence-speaks-python-project XXXXX$ curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{"message": "Hello, World!"}'
{"message":"Hello, World!","timestamp":"2025-01-18T18:15:09.525414+00:00"}
```

---

## Testing

Each program includes unit tests to verify functionality.

### Connected Cities Checker
To run test, use:
`python3 -m unittest connected_cities/tests/connected_cities_test.py`

### Simple Race Simulation
To run test, use:
`python3 -m unittest race_simulation/tests/race_sim_test.py`

### REST API
To run test, use:
`python3 -m unittest rest_microservice/tests/test_routes.py`

---

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/users/RoBizMan/projects/7) served as an Agile tool for this project.
It isn't a specialised tool, but with the right tags and project creation/issue assignments, it can work.

Through it, user stories, issues, and milestone tasks were planned and tracked weekly using the basic Kanban board.

### GitHub Issues

[GitHub Issues](https://github.com/RoBizMan/silence-speaks-python-project/issues) served as another Agile tool.

It also helped with milestone iterations.

- [Open Issues](https://github.com/RoBizMan/silence-speaks-python-project/issues) [![GitHub issues](https://img.shields.io/github/issues/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/issues)

- [Closed Issues](https://github.com/RoBizMan/silence-speaks-python-project/issues?q=is%3Aissue%20state%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/issues?q=is%3Aissue%20state%3Aclosed)

---

## GitHub **Issues**

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ARoBizMan%2Fsilence-speaks-python-project%20label%3Abug&label=bugs)](https://github.com/RoBizMan/silence-speaks-python-project/issues?q=is%3Aissue%20label%3Abug)

[![GitHub closed issues](https://img.shields.io/github/issues-closed/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/issues?q=is%3Aissue+is%3Aclosed)

All previously closed/fixed bugs can be tracked [here](https://github.com/RoBizMan/silence-speaks-python-project/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| - | - |
| [Race simulation no maximum races simulation](https://github.com/RoBizMan/silence-speaks-python-project/issues/19) | Closed |

### Open Issues

[![GitHub issues](https://img.shields.io/github/issues/RoBizMan/silence-speaks-python-project)](https://github.com/RoBizMan/silence-speaks-python-project/issues)


Any remaining open issues can be tracked [here](https://github.com/RoBizMan/silence-speaks-python-project/issues).

No open issues so far.

### Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.

---

## Credits

| Source | Notes |
| - | - |
| [Stack Overflow](https://stackoverflow.com/questions/62684227/pros-and-cons-of-different-implementations-of-graph-adjacency-list/62684297#62684297) | Pros and cons of different implementations of graph adjacency list |
| [Geeks for Geeks](https://www.geeksforgeeks.org/graph-types-and-applications/?ref=lbp) | Types of Graphs with Examples |
| [Vaidehi Joshi](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8) | A Gentle Introduction to Graph Theory |
| [Reddit ](https://www.reddit.com/r/Python/comments/64vm47/best_way_to_represent_graph_data_structure_in/) | Best way to represent Graph data structure in Python |
| [Geeks for Geeks](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/) | Difference between BFS and DFS |
| [Dgraph](https://dgraph.io/blog/post/depth-first-search-vs-breadth-first-search/) | When to Use Depth First Search vs Breadth First Search |
| [Stack Overflow](https://stackoverflow.com/questions/3332947/what-are-the-practical-factors-to-consider-when-choosing-between-depth-first-sea) | What are the practical factors to consider when choosing between Depth-First Search (DFS) and Breadth-First Search (BFS)? |
| [Python Docs](https://docs.python.org/3/library/random.html) | random - Generate pseudo-random numbers |
| [Real Python](https://realpython.com/python-random/) | Generating Random Data in Python (Guide) |
| [Cornell University](https://www.cs.cornell.edu/courses/cs1110/2016sp/lectures/03-01-16/9B.Randomness.pdf) | Cornell University - Random Simulations |
| [Co Edu](https://forum.edu.cospaces.io/t/building-a-simple-randomized-race-with-lists-and-functions/7902/6) | Building a simple randomized race with lists and functions |
| [Geeks for Geeks](https://www.geeksforgeeks.org/program-convert-speed-kmhr-msec-vice-versa/) | Program to convert speed in km/hr to m/sec and vice versa |
| [Geeks for Geeks](https://www.geeksforgeeks.org/comparison-of-fastapi-with-django-and-flask/) | Comparison of FastAPI with Django and Flask |
| [Real Python](https://realpython.com/flask-by-example-part-1-project-setup/) | Flask by Example |
| [Flask](https://flask.palletsprojects.com/en/stable/tutorial/factory/) | Application Setup |
| [Felipe Silveira](https://python.plainenglish.io/flask-restful-apis-72e05f8d41fa) | FlaskRESTful API Best Practices |
| [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis) | The Flask Mega-Tutorial, Part XXIII: Application Programming Interfaces (APIs) |
| [microapis](https://youtu.be/mt-0F_5KvQw?si=_ifio0q7dwfTHzzS) | Build APIs with Flask (the right way) |
| [Python](https://docs.python.org/3/library/unittest.html) | unittest - Unit testing framework |