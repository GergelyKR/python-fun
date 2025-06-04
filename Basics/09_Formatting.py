# format specifiers = {value.flags} format a value based on flags

# .(number)f = round to number of decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate 3 spaces, pad with 0s
# :< = left align
# :> = right align
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place the sign to leftmost position
# :  = instert a space before positive numbers
# :, = comma separator

price1 = 30000.14159
price2 = -987000.65
price3 = 12000.34

print(f"Price 1: is {price1:+,.2f}")
print(f"Price 2: is {price2:+,.2f}")
print(f"Price 3: is {price3:+,.2f}")