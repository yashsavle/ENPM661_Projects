# Project 1: 8 Puzzle Solver

The objective of this project is to develop a program to solve the classic 8 tile puzzle. The solution is found out by using Brute Force Search algorithm. The Program will try all possible moves for a current state and generate a Tree consisting of different nodes until the desired solution is obtained. Once the solution state is found, the program will backtrack the steps and store it in a list.
<p align="center">
  <img src="https://sandipanweb.files.wordpress.com/2017/03/sol_b0.gif?w=676" width="256" title="Source : https://sandipanweb.files.wordpress.com/2017/03/sol_b0.gif?w=676">
</p>



## Running the Program

There are two file in the directory 8_Puzzle.py and Plot_path.py
The files can be run through an IDE or else through terminal. Make sure you are in the same directory as the Python files.

Run the following command
```bash
python 8_puzzle.py
```
The terminal will prompt you to enter the Initial State.
Once you enter the initial state, the program will check whether the State has a solution or not. 

Refer [this](https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/) to read about the solvability condition.

If the case is solvable it will Determine the solution and generate 3 Text files.

> **nodePath.txt :** This file will contain the list of states from start node to goal node written row-wise.

> **NodesInfo.txt :** This file will contain 2 columns which has the details of a particular node, ie. individual node number and Parent node number.

> **Nodes.txt :** This file will contain list of all explored states.

In order to visualize the solution of the problem run:

```bash
python plot_path.py
```
This will provide you with the set of moves from Start node to Goal node
