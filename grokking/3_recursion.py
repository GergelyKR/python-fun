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

def greet(name): # variable for greet remains in memory until greet2 is completed.
    print("hello, " + name + "!")
    greet2(name) # when you call a function from another function, the calling function is paused in a partially completed state
    print ("getting ready to say bye...")
    bye() # bye function gets added to the top of the stack, then removed, then we return from the greet function as well

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok, bye!")

greet("Maggie")

# Call stack with recursion:

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    
# With the example of looking through boxes to find a key, a stack can keep track of the pie of boxes you already checked.
# Using this stack is convenient but it can take up a lot of memory,
# and if the stack is too tall, the memory is saving information for too many function calls.
# To solve too tall stacks, you should switch to a loop or try tail recursion if the language supports it.
    
# RECAP
# Recursion is when a function calls itself
# Every recursive function has two cases: the base case and the recursive case
# A stack has two operations: push and pop
# All function calls go onto the call stack
# The call stack can get very large, which takes up a lot of memory