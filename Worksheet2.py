# Question 1
# def check_val(x):
#     if x <= 17:
#         return 17 - x
#     return 2 * (x - 17)
# print(check_val(18))

# Question 2
# def in_range(num):
#     if 100 <= num <= 1000:
#         print("100-1000")
#     elif 1001 <= num <= 2000:
#         print("1001-2000")
#     else:
#         print("NOT IN ANY RANGE!!")
# in_range(970)

# Question 3
# def reverse_string(text):
#     print(text[::-1])
# msg = "i am Prabhjot"
# reverse_string(msg)

# Question 4
# def count_case():
#     word = input("Enter a string: ")
#     lower_count = sum(1 for ch in word if ch.islower())
#     upper_count = sum(1 for ch in word if ch.isupper())
#     print(f"LOWER : {lower_count}, UPPER : {upper_count}")
# count_case()

# Question 5
# def unique_list():
#     values = [int(input("Enter number: ")) for _ in range(5)]
#     print(list(set(values)))
# unique_list()

# Question 6
# def show_even(nums):
#     evens = [n for n in nums if n % 2 == 0]
#     print(*evens)
# data = [1,2,3,4,5,6,7,8,9]
# show_even(data)

# Question 7
# def avg(numbers):
#     return sum(numbers) / len(numbers)
# nums = [1, 2, 3, 4, 5, 6]
# print(avg(nums))
