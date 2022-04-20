# (0-1) Knapsack

**Table of contents**
1. [Problem formulation](#problem-formulation)
2. [Optimization methods](#optimization-methods)
3. [Detailed example](#detailed-example)

<a id="problem-formulation"></a>

## 1. Problem formulation
In the knapsack problem, users must select items among a list of n items in such way that:
- the total value of selected items is maximized
- the total weight of selected items does not exceed the knapsack capacity

Let:
- *n* be the number of items available
- *K* the knapsack capacity
- <img src="https://render.githubusercontent.com/render/math?math=v_i"> the value of item i
- <img src="https://render.githubusercontent.com/render/math?math=w_i"> the weight of item i

The problem can be formulated mathematically as:

*Maximize:*
 
<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} v_i * x_i">

*Subject to:*

- <img src="https://render.githubusercontent.com/render/math?math=x_i \in (0,1)">
- <img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} w_i * x_i <= K">

<a id="optimization-methods"></a>

## 2. Optimization methods

### 1. Greedy algorithm
A first approach to solve the knapsack problem is to implement a greedy algorithm. There is no guarantee that the algorithm will reach the optimal solution but it can be used to established a baseline that can then be improved with more sophisticated methods.

The greedy algorithm implemented in the repository has the following steps:
- Items are sorted in descending order by value density (i.e. items with the most value per unit of weight come first).
- User adds items to the knapsack by following the order defined in the previous step.
- The algorithm ends when no remaining item can fit in the knapsack.

### 2. Branch and bound
Now that we have established a baseline with our greedy algorithm, we will try to improve it and reach the optimal solution.

In the repository, we implement a branch and bound algorithm to find the set of items that will maximize the knapsack value. In this approach, we first solve the problem as a linear programming problem by relaxing the integrality constrainsts.

Just like with our greedy algorithm, we sort the items by descending value density. For each item, we compute the best value we could obtain if we did not have integrality constraints. If the best estimate of selecting this item exceeds the current best solution, we keep exploring this part of the tree. Otherwise, we prune the tree and explore another branch. 

### 2.1 Algorithm modeling and steps
1. Remove a node from the queue
2. Explore its 'left child' (next item in the list is selected), and compute its value, remaining capacity and best estimate.
3. If 'left child' solution does not exceed knapsack capacity and its value is greater than the current solution's best value, update current best solution.
4. If 'left child''s best estimate is greater than current best solution, add 'left child' to the list of nodes to explore.
5. Explore 'right child' (next item in the list is not selected), and compute best estimate.
6. If 'right child''s best estimate is greater than current best solution, add 'right child' to the list of nodes to explore.
7. Go back to step 1 until the queue is empty.

### 2.2 Tree exploration variants
There are several ways of exploring the search tree. This repository provides an implementation of the branch and bound with breadth-first and depth-first search methods.
#### 2.2.1. Breadth first search
In this variant, the algorithm prefers to expand all nodes of a given level before proceeding the the next level.
#### 2.2.2. Depth first search
In this variant, the algorithm will expand the nodes as deeply as possible before moving to another branch.

<a id="detailed example"></a>

## 3. Detailed example
*Coming soon*
