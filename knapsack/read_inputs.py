""" Read input files and generates dictionaries.

Files are named ks_n_i:
- n being the number of items in the problem
- i being the index in case two datasets have the same number of items

The first row of the file contains the number of items and the knapsack capacity
Each subsequent row contains the value of the item and its weight. """

path = "knapsack\\data\\"

def read_file(file_name):
    """ Reads input file and returns a list containing:
        - [0] the count of items
        - [1] the knapsack capacity
        - [3] the items
    Each item is represented by a dictionary with keys index (order in input file),
    value and weight."""

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
            lst_items.append({'index': i-1, 'value': line[0], 'weight': line[1]})

        return [count_items, capacity, lst_items]
            

print(read_file('ks_19_0'))

