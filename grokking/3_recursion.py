# Recursive function is a function that calls itself
# To avoid infinite loops, it needs a base case and a recursive case
# Example:
# def count_down(n):
#     if n == 0:
#         print("Done!")
#     else:
#         print(n)
#         count_down(n - 1)

# In the case of call stacks, inserting an item puts it on top of the list,
# and reading also only reads the topmost item, and it's taken off the list.
# It only has push (insert) and pop (remove and read) actions.