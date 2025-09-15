import math

# Question 12
# class Student:
#     def __init__(self, name, sid, section):
#         self.name = name
#         self.sid = sid
#         self.section = section
#
#     def display(self):
#         print(f"Name: {self.name}, ID: {self.sid}, Class: {self.section}")
#
# s1 = Student("Prabhjot", 1024230021, "2W13")
# s1.display()

# Question 13
# class Student:
#     def __init__(self, name, age, roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#
# st1 = Student("Prabhjot", 19, 30067)
# st2 = Student("Jashan", 19, 30000)
# print(st1.name, st1.age, st1.roll_no)
# print(st2.name, st2.age, st2.roll_no)

# Question 14
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def calc_area(self):
#         return math.pi * self.r ** 2
#
#     def calc_circumference(self):
#         return 2 * math.pi * self.r
#
# radius = int(input("Enter radius: "))
# c = Circle(radius)
# print("Area:", c.calc_area())
# print("Perimeter:", c.calc_circumference())

# Question 15
# class Word:
#     def take_input(self):
#         self.txt = input("Enter text: ")
#
#     def show_upper(self):
#         print(self.txt.upper())
#
# w = Word()
# w.take_input()
# w.show_upper()

# Question 16
# class Bot:
#     def __init__(self, model, job, battery):
#         self.model = model
#         self.job = job
#         self.battery = battery
#
#     def work(self):
#         self.battery -= 10
#         print(f"Task: {self.job}, Battery left: {self.battery}")
#
#     def charge(self):
#         self.battery = 100
#         print(f"Battery recharged to {self.battery}")
#
#     def info(self):
#         print(f"Name: {self.model}, Job: {self.job}, Battery: {self.battery}")
#
# robo = Bot("Jarvis", "Cleaning", 50)
# robo.info()
# robo.work()
# robo.charge()
