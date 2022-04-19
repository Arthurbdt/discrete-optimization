# (0-1) Knapsack

**Table of contents**
1. [Problem formulation](#problem-formulation)
1. [Optimization methods](#optimization-methods)

<a id="problem-formulation"></a>

## 1. Problem formulation
In the knapsack problem, users must select items among a list of n items in such way that:
- the total value of selected items is maximized
- the total weight of selected items does not exceed the knapsack capacity

Let:

- $n$ be the number of items available

- $K$ the knapsack capacity

- $v_i$ the value of item i

- $w_i$ the weight of item i

The problem can be formulated mathematically as:

*Maximize* $\sum_{i=1}^{n} v_i * x_i$

*Subject to:*

- $x_i \in (0,1) $

- $\sum_{i=1}^{n} w_i * x_i <= K $



<a id="optimization-methods"></a>

## 2. Optimization methods

### 1. Greedy algorithm

### 2. Branch and bound

#### 2.1. Breadth first search
#### 2.2. Depth first search