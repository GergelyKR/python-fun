names = []

with open("d:\\Code\\python-fun\\cs50p\\names.txt") as file:
    # for line in sorted(file): -> if we don't want to modify data while iterating
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"hello, {name}")