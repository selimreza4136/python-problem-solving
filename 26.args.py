# * args
#Q1. Write a function print_all(*args) that accepts an arbitrary number of arguments
# and prints each argument on a new line using a for loop. Test it by passing three strings:
# "Python", "Data", and "Science"

def print_all(*args):
    for string in args:
        print(string)

