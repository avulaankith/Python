#This code submitted by A.Ankith Reddy and group as a part of AI Search Assignment.
#The problem is to rearrange the numbers in a 3x3 square, so that it forms a magicsquare and the program is done in python programming language.

So the initial state = [[1,2,3],[4,5,6],[7,8,9]] and the goal state = [[2,7,6],[9,5,1],[4,3,8]]

The path in which the solution determines the correct answer with least cost per each move is considered to be the optimal solution for this problem.

The initial_list is replicated and 4 copies are maintained.

For this purpose, we need to define some of the functions. They are as follows:
1. calculate_cost ---> finds the cost of each move by calling a function finding_nemo within it
2. finding_nemo -----> this function actually calculates the cost of each move. It is being called in other function calculate_cost.
3.find_coordinates --->  returns the coordinates of the value which has least cost to move (other than 0)
4.start_movement ----> prints the total number of possible moves for a suitable block/value from it's position to the desired position.
5.move_down ----> moves the current block to 1 step down
6.move_up -----> moves the current block to 1 step up
7.move_right ---->moves the current block to 1 step right
8.move_left ----->moves the current block to 1 step left

cost_list stores the list of costs of all elements (seems to be a list or a 1-D array)
cost_sum stores the sum of all elements in cost_list 
