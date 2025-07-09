# DIVIDE & CONQUER
# 2 steps:
# 1. Figure out the base (simplest possible) case
# 2. Divide or decrease your problem until it becomes the base case
# With every recursive call, you have to reduce your problem

# "If you find the biggest box that will work for this size,
# that will be the biggest box that will work for the entire farm."

# Tip -> When you are writing a recursive function involving an array,
# the base case is often an empty array or an array with one element.

# ---

# QUICKSORT
# Pick an element from the array (pivot)
# Find elements smaller and larger than the pivot (partitioning)
# Now you have:
# - Sub-array of all the numbers less than the pivot
# - The pivot
# - Sub-array of all the numbers greater than the pivot

# Quicksort the sub-arrays with base case and combine results for a sorted array

def quicksort(array):
    if len(array) < 2:
        return array # Base case, arrays with 0 or 1 element are already "sorted"
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # Sub-array of all the numbers less than the pivot
        greater = [i for i in array[1:] if i > pivot] # Sub-array of all the numbers greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 5, 2, 3]))

# If you choose a random pivot, the running time is O(n log n) -> best case
# O(n) * O(log n) = O(n log n)
# In the worst case, there are O(n) levels, so the algorithm will take O(n^2) time
# O(n) * O(n) = O(n^2)

# RECAP
# - D&C works by breaking a problem down into smaller and smaller pieces.
#   If you're using D&C on a list, the base case is probably an empty array or an array with one element.
# - If you're implementing quicksort, choose a random element as the pivot.
#   The average runtime of quicksort is O(n log n).
# - The constant (fixed amount of time the algorithm takes) in Big O notation can matter sometimes.
#   That's why quicksort is faster than merge sort.
# - The constant almost never matters for simple search vs. binary search
#   because O(log n) is much faster than O(n) with bigger lists.