
#Q1. Define a global variable x = 100. Inside a function show_x(), print x. Call show_x()
# to demonstrate that global variables are accessible inside functions

# x = 100
# def show_x():
#     print(f"Iside function: {x}")
#
# show_x()
# print(f"Outside function: {x}")

#Q2. Create a function set_local() that defines a variable y = 50 inside its body.
# Attempt to print y outside the function and explain what error occurs

def set_local():
    y = 50

set_local()
try:
    print(y)
except NameError as e:
    print(f"Caught Error: {e}")

#Q3.

