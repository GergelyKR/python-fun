# Example for dynamic programming with grid for knapsack problem
# You have a grid, each row for an item, each column for an unit of weight to capacity

def knapsack(wt, val, W, n): 

    # base conditions 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 

    # choice diagram code 
    if wt[n-1] <= W: 
        t[n][W] = max( 
            val[n-1] + knapsack( 
                wt, val, W-wt[n-1], n-1), 
            knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapsack(wt, val, W, n-1) 
        return t[n][W] 

# Driver code 
if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
    
    # We initialize the matrix with -1 at first. 
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
    print(knapsack(weight, profit, W, n)) 


# RECAP

# Dynamic programming is a technique for solving problems by breaking them down into subproblems and solving them recursively
# Useful when trying to optimize something given a constraint
# Every dynamic-programming solution involves a grid
# The values in the cells are usually what you're trying to optimize
# Each cell is a subproblem, so think about how you can divide your problem into subproblems
# There's no single formula for calculating a dynamic-programming solution