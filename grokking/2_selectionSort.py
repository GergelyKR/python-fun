# Storing multiple items in memory can be done with arrays and lists.
# They work differently. Arrays are stored in a row of memory, linked lists are not stored together, they each contain the address of the next item.

# Common operations comparison:

#               Arrays      Lists
# reading       O(1)        O(n)
# insertion     O(n)        O(1)
# deletion      O(n)        O(1)

# Arrays allow random access, lists only allow sequential access.
# Linked lists are good for inserts / deletes, arrays are faster for random access.
# Hybrid data structure (FB example): Array of linked lists. Array with 26 slots, each points to a linked list containing a particular letter

# SELECTION SORT for example to sort an array from smallest to largest

def FindSmallest(arr):
    smallest = arr[0] # Stores smallest value
    smallest_index = 0 # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = FindSmallest(arr)     # Finds the smallest element in the array,
        newArr.append(arr.pop(smallest)) # and adds it to the new array
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

# RECAP
# The computer's memory is like a giant set of drawers
# When you want to store multiple elements, use an array or a list
# With an array, all your elements are stored right next to each other
# With a list, elements are strewn all over, and one element stores the address of the next one
# Arrays allow fast reads
# Linked lists allow fast inserts and deletes
# All elements in the array shoul be the same type (all ints, all doubles, etc.)