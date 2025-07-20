def meow(n: int) -> str:
    # Docstring: Convention to document functions using standard syntax
    """
    Meow n times.
    
    :param n: The number of times to meow.
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """


    return "meow\n" * n


number: int = int(input("How many meows? "))
meows: str = meow(number)
print(meows, end="")