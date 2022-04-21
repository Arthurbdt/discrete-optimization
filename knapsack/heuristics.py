def solve_greedy(items, capacity):
    """
    Runs a simple heuristic to attempt to solve the knapsack problem.
    Heuristic sorts the items by their value density (i.e. value / weight) descending
    and adds items to the solution until there is no capacity left for any other item.
    """
    items = sorted(items, key = lambda i: i['weight'] / i['value'] )
    selected = [0]*len(items)
    value = 0

    for i in items:
        if capacity - i['weight'] >= 0:
            capacity -= i['weight']
            value += i['value']
            selected[i['index']] = 1

    return selected, value
