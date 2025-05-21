# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in reversed(range(1, 11)):
    print(x)

print("Happy New Year!")

for x in range(1, 21):
    if x == 13:
        continue # skip this number
        # break = exit the entire loop
    else:
        print(x)