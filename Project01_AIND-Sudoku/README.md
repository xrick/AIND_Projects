# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked twins allows us to use constraint propagation in solving the sudoku puzzle because there are often times peers which can each be one of the same two things. This means each of those peers must be one of those two things, so none of their mutual set of peers can be either of those two things. This means the twins mutual set of peers can have those two possibilities eliminated and thus constraints propagate across the board and reduce the search space as twins are discovered.
# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We use constraint propagation to solve the diagonal sudoku problem by adding extra units to represent the diagonals. This means that each box which belongs to a diagonal unit will have the numbers it could possibly be filled in by constrained by every other box along its diagonal. Most of the boxes aren't directly affected by this, since the diagonals units don't contain most of the boxes, but this is a useful constraint for the boxes which do belong to diagonal units- since they can potentially have fewer possible options during the search phase. Even boxes which don't belong to the diagonal units directly do belong to the same units as boxes which are part of the diagonal units, so those could be indirectly affected in a positive way as well.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - Fill in the required functions in this file to complete the project.
* `test_solution.py` - You can test your solution by running `python -m unittest`.
* `PySudoku.py` - This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

