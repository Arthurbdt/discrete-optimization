""" 
Load data file and solve knapsack problem
"""
import read_inputs as inp
import branch_bound as bb
import heuristics as hr

# read problem data
file_name = 'ks_19_0'
data = inp.read_file(file_name)

# visualize input data
df = inp.create_df(data)
inp.print_histogram(df)

# solve knapsack with greedy heuristics
baseline = hr.solve_greedy(data[2], data[1])
print(f'Greedy algorithm reached a value of {baseline[1]} with the following items: {baseline[0]}')


# solve knapsack with branch and bound
solved = bb.solve_bb(data[2], data[1], 'best')
print(f'Branch and bound algorithm reached a value of {solved[1]} with the following items {solved[0]}')

# compare solutions
delta = round(((solved[1] / baseline[1]) - 1)*100,2)
print(f'Branch and bound algorith improved baseline solution by {delta} %')


