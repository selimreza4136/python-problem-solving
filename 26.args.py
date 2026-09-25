# * args
#Q1. Write a function print_all(*args) that accepts an arbitrary number of arguments
# and prints each argument on a new line using a for loop. Test it by passing three strings:
# "Python", "Data", and "Science"

# def print_all(*args):
#     for string in args:
#         print(string)
# print_all("Python", "Data", "Science")

#Q2. Create a function sum_numbers(*args) that takes any quantity of numbers, sums them up
# using the built-in sum() function, and returns the total. Call it with (10, 20, 30, 40)

# def sum_numbers(*args):
#     return sum(args)
#
# print(sum_numbers(10,20,30,40))

#without sum() function
# def sum_numbers(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# print(sum_numbers(10, 20, 30, 40))

#Q3. Write a function calculate_average(first_num, *args) that requires at least one
# positional argument (first_num) and optionally accepts additional numbers in *args.
# Calculate and return the average of all provided numbers
# def calculate_average(first_num, *args):
#     total = (first_num,) + args
#     return sum(total) / len(total)
#
# average = calculate_average(10,20,30,40,50)
# print(f"Average of given positional and args: {average}")

#
# def calculate_average(first_num, *args):
#     total = (first_num,) + args
#     return sum(total) / len(total)
#
# average = calculate_average(1,2,3,4,5,67,9)
# print(average)
#
# def calculate_average(first_num, *args):
#     total = (first_num, ) + args
#     return sum(total) / len(args)
#
# average = calculate_average(1,2,3,4,5,6,7,8,9)
# print(average)

#Q4. Demonstrate argument unpacking using *. Given a list num_list = [5, 10, 15, 20],
# pass num_list into sum_numbers(*args) using the unpack operator *num_list and
# print the result

# def sum_numbers(*args):
#     return sum(args)
#
# num_list = [5,10,15,20]
# result = sum_numbers(*num_list)
# print(f"Sum of numbers: {result}")

#practice
# def sum_numbers(*args):
#     return sum(args)
#
# num_list = [5,10,15,20]
# result = sum_numbers(*num_list)
# print(f"Sum of numbers: {result}")
