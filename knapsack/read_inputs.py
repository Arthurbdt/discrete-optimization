""" 
Read and analyze problem input files.

Files are named ks_n_i:
- n being the number of items in the problem
- i being the index in case two datasets have the same number of items

The first row of the file contains the number of items and the knapsack capacity
Each subsequent row contains the value of the item and its weight. 
"""

import matplotlib.pyplot as plt
import pandas as pd

path = "knapsack\\data\\"

def read_file(file_name):
    """ 
    Read input file and return a list containing:
        - [0] the count of items
        - [1] the knapsack capacity
        - [2] the items
    Each item is represented by a dictionary with keys index (order in input file),
    value and weight.
    """

    with open(path + file_name, 'r') as file: 
        data = file.read().split('\n') # read file and remove \n

        # retrieve problem data
        line1 = data[0].split() # split first line at the space
        count_items = int(line1[0])
        capacity = int(line1[1])

        # retrieve list of items
        lst_items = []
        for i in range(1, count_items + 1):
            line = data[i].split() # spliut item line at space
            lst_items.append({'index': i-1, 'value': float(line[0]), 'weight': float(line[1])})

        return [count_items, capacity, lst_items]
            

def create_df(data):
    """ 
    Convert input data into a pandas dataframe.
    """
    df = pd.DataFrame(data[2])
    df = df.astype({'value': float, 'weight': float})
    df['density'] = df['value'] / df['weight']  # items value per unit of weight
    return df


def print_scatter(df):
    """ 
    Generate a scatter plot of items value and weight.
    """
    plt.figure(dpi=100)
    plt.title('Items value against items weight')
    plt.xlabel('Items weight')
    plt.ylabel('Items value')
    plt.grid(color='gray', linestyle='-', linewidth=.15)
    plt.scatter(df['weight'], df['value'])
    plt.show()

def print_histogram(df):
    """ 
    Generate a histogram of items density.
    """
    plt.figure(dpi=100)
    plt.title('Items value against items weight')
    plt.grid(color='gray', linestyle='-', linewidth=.15)
    plt.hist(df['density'])
    plt.show()

