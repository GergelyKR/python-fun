# nested loop = a loop within another loop (outer, inner)
#              outer loop:
#                  inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows): # we need 3 iterations
    for y in range(columns): # counter has to be different
        print(symbol, end="") # end = override default newline
    print() # print a newline after the inner loop