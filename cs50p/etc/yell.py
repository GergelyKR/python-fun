# map: allows to apply a function to each element of an iterable

def main():
    yell("This", "is", "CS50")

def yell(*words):
    # uppercased = map(str.upper, words) -> Using mapping, iterate each word and call the function on them
    uppercased = [word.upper() for word in words] # Using list comprehension, defining a list on the fly, no need to append
    print(*uppercased)


if __name__ == "__main__":
    main()