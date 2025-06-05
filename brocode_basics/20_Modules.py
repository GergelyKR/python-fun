# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

import math
# import math as m -> renames the module for convenience
# from math import pi -> adds the function into the namespace, can cause name conflicts with other variables
print(math.pi)

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

print()
# ---

import example

result = example.pi
print(result)

print(example.square(3))
print(example.circumference(3))
print(example.area(3))
print(example.cube(3))