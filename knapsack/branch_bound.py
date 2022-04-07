"""
Add description of module
"""


class Node:
    """
    Node of the tree
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
    # check whether current node has not exceeded capacity ### NOT REQUIRED?
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
    # create original node
    root = Node(-1, capacity, 0, [])
    queue = [root]
    current_max_value = 0

    # start iteration
    while len(queue) > 0:
        parent = queue.pop(0)

        # create left node - select next item
        left = Node(None, None, None, None)
        left.level = parent.level + 1
        left.capacity = parent.capacity - items[left.level]['weight'] 
        left.value = parent.value + items[left.level]['value']
        left.in_knapsack = parent.in_knapsack
        left.in_knapsack.append(items[left.level]['index'])

        # check if left node is worth exploring
        if (left.capacity >=0) and left.value > current_max_value: #maybe > instead of >=
            current_max_value = left.value
            # compute best estimate
            left.bound = bound(left, items)  # this will need to be modified
            # if best estimate is greater than current solution, add to the queue
            if left.bound > current_max_value:
                queue.append(left)
                current_best_items = left.in_knapsack
        
        # create right node - do not select next item
        right = Node(None, None, None, None)
        right.level = parent.level + 1
        right.capacity = parent.capacity
        right.value = parent.value
        right.in_knapsack = parent.in_knapsack
        right.bound = bound(right, items)

        # if best estimate is greater than current solution, add to the queue
        if right.bound > current_max_value:
            queue.append(right) 

    # end of the iteration
    selected = [0] * len(items)
    for i in current_best_items:
        selected[i] = 1

    return selected





