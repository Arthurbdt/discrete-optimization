class Node:
    """
    Store information regarding the node to explore
    """
    def __init__(self, level, capacity, value, items):
        self.level = level
        self.capacity = capacity
        self.value = value
        self.in_knapsack = items

def bound(node, items):
    """
    Compute the best value estimate using relaxation of {0-1} constraint
    """
    if node.capacity < 0:
        return 0
    else:
        value = node.value
        level = node.level + 1 # start iteration with next object in list
        capacity = node.capacity

        for i in items[level:]:
            if capacity - i['weight'] > 0:
                capacity -= i['weight']
                value += i['value']
            else:
                value += i['value'] * capacity / i['weight']
                capacity = 0
    return value

def solve_bb(items, capacity):
    """
    Implementation of branch and bound algorith for (0-1) knapsack problem

    Args:
    - items: list containing one dictionary for each item available. Each dict
    must have these 3 keys: index, value and weight. The list must be sorted by
    (value / weight) in decreasing order
    - capacity: the total capacity of the knapsack

    Returns:
    - selected: list of {0-1} indicating whether item of current index has been selected
    - value: total value stored in knapsack
    """
    items = sorted(items, key = lambda i: i['weight'] / i['value'] )

    # create root of the tree and add to exploration queue
    root = Node(-1, capacity, 0, [])
    queue = [root]
    current_max_value = 0

    # start iteration
    while len(queue) > 0:
        parent = queue.pop(0)

        # create left node (i.e. select next item)
        left = Node(None, None, None, None)
        left.level = parent.level + 1
        left.capacity = parent.capacity - items[left.level]['weight'] 
        left.value = parent.value + items[left.level]['value']
        left.in_knapsack = list(parent.in_knapsack)
        left.in_knapsack.append(items[left.level]['index'])

        # check whether current solution can be set as best solution
        if (left.capacity >=0) and left.value > current_max_value:
            current_max_value = left.value
            current_best_items = left.in_knapsack
                
        # if best estimate is greater than current solution, add to the queue
        left.bound = bound(left, items)
        if left.bound > current_max_value:
            queue.append(left)
        
        # create right node (i.e. do not select next item)
        right = Node(None, None, None, None)
        right.level = parent.level + 1
        right.capacity = parent.capacity
        right.value = parent.value
        right.in_knapsack = list(parent.in_knapsack)
        right.bound = bound(right, items)

        # if best estimate is greater than current solution, add to the queue
        if right.bound > current_max_value:
            queue.append(right) 

    # end of the iteration
    selected = [0] * len(items)
    for i in current_best_items:
        selected[i] = 1

    return selected, current_max_value





