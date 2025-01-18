# Silence Speaks Python Project

This repository contains my solutions to the Python coding project provided by Silence Speaks.

## Table of Contents
- [Connected Cities Checker](#connected-cities-checker)
- [Running the Programs](#running-the-programs)
- [Testing](#testing)
- [Credits](#credits)

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

## Testing

Each program includes unit tests to verify functionality.

### Connected Cities Checker
To run test, use:
`python3 -m unittest connected_cities/tests/connected_cities_test.py`

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