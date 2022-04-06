""" 
Load data file and solve knapsack problem
"""

import read_inputs as inp

def solve_with_heuristic(data):
    """
    Runs a simple heuristic to attempt to solve the knapsack problem.
    Heuristic sorts the items by their value density (i.e. value / weight) descending
    and adds items to the solution until there is no capacity left for any other item.

    Prints the knapsack value, capacity remaining and whether each item has been selected.
    """
    # load problem data
    num_items = data[0]
    capacity = data[1]
    items = data[2]
    print(f'Number of available items: {num_items}')
    print(f'Knapsack capacity: {capacity}')

    # heuristic
    items = sorted(items, key = lambda i: i['weight'] / i['value'] )
    selected = [0]*num_items
    value = 0
    for i in items:
        if capacity - i['weight'] >= 0:
            capacity -= i['weight']
            value += i['value']
            selected[i['index']] = 1

    # return solution
    print(f'Value in knapsack: {value}')
    print(f'Capacity remaining: {capacity}')
    print(f'Selected items: {selected}')

# load data and execute solver
file_name = 'ks_200_0'
data = inp.read_file(file_name)
solve_with_heuristic(data)