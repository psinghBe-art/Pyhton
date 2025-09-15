import math as m

# Question 1
# print("Twinkle, twinkle, little star, How I wonder what you are!\n"
#       "\tUp above the world so high, Like a diamond in the sky.\n"
#       "\t\tTwinkle, twinkle, little star, How I wonder what you are!")

# Question 2
# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# print(f"{last} {first}")

# Question 3
# radius = float(input("Radius: "))
# area = m.pi * (radius ** 2)
# print(f"Circle area = {area:.2f}")

# Question 4
# colors = ["Red", "Green", "White", "Black"]
# print("First:", colors[0], "Last:", colors[-1])

# Question 5
# num = int(input("Enter a number: "))
# s = str(num)
# result = num + int(s*2) + int(s*3)
# print(f"{num}+{s*2}+{s*3} = {result}")

# Question 6
# numbers = [int(input(f"Enter value {i+1}: ")) for i in range(5)]
# print("List:", numbers)
# print("Tuple:", tuple(numbers))

# Question 7
# celsius = float(input("Celsius: "))
# fahrenheit = (9/5) * celsius + 32
# print(f"{celsius}°C = {fahrenheit}°F")

# Question 8
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Before Swap:", x, y)
# x, y = y, x
# print("After Swap:", x, y)

# Question 9
# n = int(input("Enter number: "))
# print("Even" if n % 2 == 0 else "Odd")

# Question 10
# year = int(input("Year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# Question 11
# x1, y1 = map(int, input("Enter x1 y1: ").split())
# x2, y2 = map(int, input("Enter x2 y2: ").split())
# distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
# print(f"Distance = {distance:.2f}")

# Question 12
# angles = [int(input(f"Enter angle {i+1}: ")) for i in range(3)]
# print("Valid Triangle" if sum(angles) == 180 else "Invalid Triangle")

# Question 13
# p = float(input("Principal: "))
# r = float(input("Rate %: "))
# t = float(input("Time (years): "))
# n = int(input("Compounds per year: "))
# amt = p * (1 + r/(100*n))**(n*t)
# print(f"Compound Interest = {amt-p:.2f}")
# print(f"Final Amount = {amt:.2f}")

# Question 14
# num = int(input("Enter number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")

# Question 15
# n = int(input("Enter n: "))
# formula = n * (n+1) * (2*n+1) // 6
# print("Sum of squares:", formula)
