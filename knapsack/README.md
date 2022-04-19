# (0-1) Knapsack

**Table of contents**
1. [Problem formulation](#problem-formulation)
2. [Optimization methods](#optimization-methods)
3. [Running the code](#run-the-code)

<a id="problem-formulation"></a>

## 1. Problem formulation
In the knapsack problem, users must select items among a list of n items in such way that:
- the total value of selected items is maximized
- the total weight of selected items does not exceed the knapsack capacity

Let:

- n be the number of items available

- K the knapsack capacity

- vi the value of item i

- wi the weight of item i

The problem can be formulated mathematically as:

*Maximize* 
$\sum_{i=1}^{n} v_i * x_i$

<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} v_i * x_i">

*Subject to:*

- $x_i \in (0,1) $

- $\sum_{i=1}^{n} w_i * x_i <= K $



<a id="optimization-methods"></a>

## 2. Optimization methods

### 1. Greedy algorithm
A first approach to solve the knapsack problem is to implement a greedy algorithm. There is no guarantee that the algorithm will reach the optimal solution but it can be used to established a baseline that can then be improved with more sophisticated methods.

The greedy algorithm implemented in the repository has the following steps:
- Items are sorted in ascending by value density (i.e. items with the most value per unit of weight come first).
- User adds items to the knapsack by following the order defined in the previous step.
- The algorithm ends when no remaining item can fit in the knapsack.

### 2. Branch and bound

#### 2.1. Breadth first search
#### 2.2. Depth first search

<a id="run-the-code"></a>

## 3. Running the code
*Coming soon*
