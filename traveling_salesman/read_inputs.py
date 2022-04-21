""" 
Read and analyze input files for traveling salesman problem.

Files are named tsp_n_i:
- n being the number of cities to be visited
- i being the index in case two datasets have the same number of items

The first row of the file contains the number of cities in the problem
Each subsequent row contains the the x and y coordinates of each city
"""

import matplotlib.pyplot as plt
import pandas as pd

path = "traveling_salesman\\data\\"

def read_file(file_name):
    """ 
    Read input file and return a list containing the coordinates of each city

    Each city is represented by a list with their x coordinate in index 0 and y
    coordinate in index 1
    """

    with open(path + file_name, 'r') as file: 
        data = file.read().split('\n') # read file and remove \n
        line1 = data[0].split()
        num_cities = int(line1[0])  # read number of cities from file

        # record coordinates of each city
        lst_cities = []
        for i in range(1, num_cities + 1):
            line = data[i].split()
            index = i-1
            x = float(line[0])
            y = float(line[1])
            lst_cities.append([index, x, y])

        return lst_cities

def plot_cities(data):
    """
    Print a scatter plot of all cities in the problem
    """
    df = pd.DataFrame(data)
    plt.scatter(df[1], df[2])
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')
    plt.title("Map of cities on the route")
    plt.show()
