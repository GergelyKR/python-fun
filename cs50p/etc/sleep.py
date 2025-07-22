def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    # flock = []
    # for i in range(n):
    #     flock.append("🐑" * i)
    # return flock
    for i in range(n):
        yield "🐑" * i # Return one value at a time, save memory and processing power
        # yield is returning an iterator that allows code to iterate over generated values one at a time
        # yield returns result after every iteration, not just at the very end of the loop


if __name__ == "__main__":
    main()