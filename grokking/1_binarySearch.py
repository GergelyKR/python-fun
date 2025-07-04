# log10 100 is like asking "How many 10s do we multiply together to get 100?"
# The answer is 2: 10 x 10. So log10 100 = 2. (Logs are the flip of exponentials.)
# 
# log10 100 = 2   -> 10^2 = 100
# log10 1000 = 3  -> 10^3 = 1000
# log2 8 = 3      -> 2^3 = 8
# log2 16 = 4     -> 2^4 = 16
# log2 32 = 5     -> 2^5 = 32

# ---

# array -> Sequence of elements in a row of consecutive buckets

# - binary_search takes a sorted array and an item. If the item is in the array, the function returns its position. You'll keep track
# - of what part of the array you have to search through. At the beginning, this is the entire array:
# low = 0
# high = len(list) - 1
# 
# - each time, you check the middle element:
# mid = (low + high) / 2
# guess = list[mid]
# 
# - if the guess is too low, you update low accordingly:
# if guess < item:
#     low = mid + 1

# - if the guess is too high, you update high.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # -> 1 (The list start at 0, the second slot has index 1.)
print(binary_search(my_list, -1)) # -> None (None means nil in Python, the item wasn't found)

# Exercise 1. -> A sorted lost of 128 names, what are the maximum steps? (7)
# Exercise 2. -> A sorted lost of 256 names, what are the maximum steps? (8)

# ---

# RUNNING TIME marks the efficiency of the algoritm.
# Simple search -> 100 items takes 100 guesses, the number of guesses is the same as the size of the list. This is called linear time, O(n).
# Binary search -> 100 items takes 7 guesses, the number of guesses is the log of the size of the list. This is called logarithmic time, O(log n).

# BIG O NOTATION helps us to compare the running time of different algorithms so we can tell how the running time increases as the list size increases.
# Big O doesn't tell you the speed in seconds, it lets you compare the number of operations and tells how fast the algorithm grows.

#                simple search  |  binary search
#   100 items           100ms   |  7ms
# 10000 items           10 secs |  14ms

# Big O -> O(n) where n means number of operations
# Big O establishes a worst-case run time

# COMMON BIG O run times
# O(log n) also known as log time. Example: binary search
# O(n) also known as linear time. Example: simple search
# O(n * log n) Example: A fast sorting alogritm, like quick sort
# O(n^2) Example: A slow sorting algorithm, like selection sort
# O(n!) Example: A really slow algorithm, like a traveling salesperson -> Checking the shortest travel order between 5 cities is O(5!)

# RECAP
# Binary search is a lot faster than simple search
# O(log n) is faster than O(n) but it gets a lot faster as the list of items grows
# Algorithm speed isn't measured in seconds
# Algorithm times are measured in terms of growth of an algorithm
# Algorithm times are written in BIG O notation

