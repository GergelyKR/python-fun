# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step] -> starting index is inclusive

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4]) # 1234
# print(credit_number[:4]) # 1234
# print(credit_number[5:9]) # 5678
# print(credit_number[5:]) # from 5 to the end of string
# print(credit_number[-1]) # -2, -3... print from the end of string
# print(credit_number[::2]) # every second character

# Last for digits of a credit card number

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse_credit_number = credit_number[::-1] # -1 step reverses string
print(f"Reversed credit number: {reverse_credit_number}")