# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local, Enclosing, Global, Built-in
# local = only available in the function itself

def func1():
    # x = 1 -> if this is not present, the global x will be used

    def func2():
        # x = 2 -> if this is not present, it will use x = 1 from func1
        print(x)
    func2()

x = 3
func1()

from math import e

# e = 5 -> if this is not present, the built-in e from math will be used

def func3():
    print(e)