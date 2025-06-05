# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs."
    print(f"Your weight is: {round(weight,1 )} {unit}")
elif unit == "L":
    weight = weight / 2.20462
    unit = "Kgs."
    print(f"Your weight is: {round(weight,1 )} {unit}")
else:
    print(F"{unit} was not valid")

T_unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))

if T_unit == "C":
    temp = round((temp * 9 / 5) + 32, 1)
    print(f"Temperature in Fahrenheit: {temp}°F")
elif T_unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Temperature in Celsius is {temp}°C")
else:
    print(f"{T_unit} is an invalid unit of measurement.")