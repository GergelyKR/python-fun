# *args     = allows to pass multiple non-key arguments -> tuple
# **kwargs  = allows to pass multiple keyword-arguments -> dictionary
#             * unpacking operator
#             1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*args): # * is required, name can be changed
    sum = 0
    for arg in args:
        sum += arg
    return(sum)

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
print()

def print_address(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")

# ---
print()
print()

def shipping_label(*args, **kwargs): # args come first
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")}, {kwargs.get("state")} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")