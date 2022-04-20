def solve_greedy(data):
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
    return selected, value
