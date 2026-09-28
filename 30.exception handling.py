# exception handling
#Q1. Write a function safe_divide(a, b) that attempts to divide a by b. Use a try-except
# block to catch a ZeroDivisionError and return "Cannot divide by zero" if b is 0

# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
# print(safe_divide(10,2))
# print(safe_divide(10,0))

#practice
# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
# print(safe_divide(10,2))
# print(safe_divide(10,0))
#Q2. Write a snippet that prompts or takes a input string "abc" and attempts to convert it
# to an integer using int(). Catch the ValueError and print "Invalid number format"

# x = "abc"
# try:
#     print(int(x))
# except ValueError:
#     print("Invalid number format")

#Q3. Demonstrate handling multiple specific exceptions. Write a function
# get_element(lst, index) that accesses lst[index]. Catch both IndexError
# (if index is out of bounds) and TypeError (if index is not an integer),
# returning an appropriate error message for each

# def get_element(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         return "IndexError: index is out of bounds"
#     except TypeError:
#         return "NameError: index is not an integer"
#
# num = [10,20,30]
# print(get_element(num, 1))
# print(get_element(num, 7))
# print(get_element(num, "a"))

#practice
# def get_element(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         return "IndexError: index is out of range"
#     except TypeError:
#         return "TypeError: list indices must be integers"
# data = [20, 30, 40, 50]
# print(get_element(data,1))
# print(get_element(data,5))
# print(get_element(data,"a"))

#Q4. Demonstrate the use of else and finally blocks. Create a snippet that attempts a valid
# division (e.g., 10 / 2), prints the result in the else block, and prints
# "Execution completed." in the finally block regardless of whether an exception occurred

# numerator = int(input("Enter an integer: "))
# denominator = int(input("Enter an integer: "))
#
# try:
#     divide = numerator / denominator
#     print(divide)
# except ZeroDivisionError:
#     print("Division is not possible")
#
# except ValueError:
#     print("Enter only numbers")
# else:
#     print(divide)
# finally:
#     print("Execution completed.")


#Alternative

# def  divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Zero division detected")
#     except TypeError:
#         print("Enter number only")
#     else:
#         print(result)
#     finally:
#         print("Execution completed.")
#
# divide(5,2)
# divide(10, 0)
# divide(10,"a")

#Q5. Write a custom exception class NegativeAgeError(Exception). Then write a function
# set_age(age) that raises NegativeAgeError("Age cannot be negative") if age < 0.
# Test set_age(-5) using a try-except block to catch and print your custom error message.

# class NegativeAgeError(Exception):
#     pass
#
# def set_age(age):
#     if age < 0:
#         raise NegativeAgeError("Age cannot be negative")
#     return f"Age set successfully: {age}"
#
# try:
#     print(set_age(25))
#     print(set_age(-5))
# except NegativeAgeError as e:
#     print(f"Custom Exception Caught: {e}")