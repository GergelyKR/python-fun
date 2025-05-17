import math

x = 9

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
result = math.sqrt(x)  # square root
result = math.ceil(x)  # round up
result = math.floor(x) # round down

print(result)

radius = float(input("Enter the radius of a circle:"))

circumference = 2 * math.pi * radius

# print(f"The circumference is: {circumference} cm")
print(f"The circumference is: {round(circumference, 2)}cm")

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")

print("Now we'll check the Pythagorean theorem.")
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {round(c ,2)}")