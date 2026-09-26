# String format
#Q1. Use positional placeholders {0} and {1} with .format() to print
# "Hello, Md. Selim Reza! Welcome to Python." by passing "Md. Selim Reza" and "Python"

# name = "Md. Selim Reza"
# language = "Python"
#
# print("Hello, {0}! Welcome to {1}".format(name, language))
#alternative

# text = "Hello, {0}! Welcome to {1}".format("Md. Selim Reza", "Python")
# print(text)


#Q2. Use named placeholders inside curly braces (e.g., {name} and {role}) with .format()
# to display "Name: Selim, Role: Analyst"

# print("Name: {name}, Role: {role}".format(name = "Selim", role = "Analyst"))

#Q3. Format a floating-point number pi = 3.14159265 to display only 2 decimal places using
# .format(). Output should be "Pi is approximately 3.14"

# pi = 3.14159265
# print("Pi is approximately {:.2f}".format(pi))

#alternative
# pi = 3.14159265
# text = "Pi is approximately {:.2f}".format(pi)
# print(text)
#Q4. Format a large integer population = 170000000 to include comma thousands separators using
# .format(). Output should be "170,000,000"

# population = 170000000
# print("Output should be {:,}".format(population))

#alternative
# population = 170000000
# formatted_pop = "Formatted population {:,}".format(population)
# print(formatted_pop)

#Q5. Given a list of items and prices [("Apple", 1.5), ("Banana", 0.75), ("Dragonfruit", 12.0)],
# write a loop using .format() with string alignment specifiers to align the item names
# left-aligned with a width of 12 characters, and prices right-aligned with a width of
# 8 characters and 2 decimal places

# items = [("Apple", 1.5), ("Banana", 0.75), ("Dragonfruit", 12.0)]
#
# for item, price in items:
#     print("{:<12} | {:>8.2f}".format(item, price))

#Practice
# items = [("Apple", 1.5), ("Banana", 0.75), ("Dragonfruit", 12.0)]
#
# for item, price in items:
#     print("{:<12} | {:>8.2f}".format(item, price))

