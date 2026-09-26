# **kwargs
#Q1. Write a function display_info(**kwargs) that accepts arbitrary keyword arguments
# and prints each key-value pair in the format Key: <key>, Value: <value>.
# Test it with name="Selim" and major="Mathematics"

# def display_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"Key: {key}, Value: {value}")
#
# display_info(name="Selim", major="Mathematics")
#practice
# def display_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"Key: {key}, Value: {value}")
# display_info(name = "Selim", major = "Mathematics")

#Q2. Create a function build_profile(**kwargs) that accepts keyword arguments and returns
# the dictionary constructed by kwargs. Call it with first="Md", last="Reza", and age=25

# def build_profile(**kwargs):
#     return kwargs
#
# profile = build_profile(first = "Md", last = "Reza", age = 25)
# print("Profile dictionary:", profile)
#practice
# def build_profile(**kwargs):
#     return kwargs
#
# profile = build_profile(first = "Md",last = "Reza", age = 25)
# print(f"Profile dictionary: {profile}")

#Q3. Write a function format_user(title, **kwargs) that takes a required positional argument
# title and arbitrary keyword arguments **kwargs. The function should return a
# formatted string combining title with all key-value pairs formatted as "key=value"

# def format_user(title, **kwargs):
#     details = ",".join(f"{k}={v}" for k, v in kwargs.items())
#     return f"[{title}], {details}"
#
# result = format_user(title = "Gavi Bittanto", author = "Ahmed Chofa", release_year = 1995)
# print(result)

#practice
# def format_user(title, **kwargs):
#     details = ", ".join(f"{k}: {v}" for k,v in kwargs.items())
#     return f"[{title}], {details}"
#
# result = format_user(title = "AI Engineer", company = "Google", skill = "Python", deadline = "23 Dec 2026")
#
# print(result)
#Q4. Demonstrate dictionary unpacking using **. Given
# user_data = {"role": "Admin", "status": "Active"}, pass user_data into
# display_info(**kwargs) using the dictionary unpack operator **user_data

# def display_info(**kwargs):
#     return kwargs
#
# user_data = {"role": "Admin", "status": "Active"}
#
# result = display_info(**user_data)
# print(user_data)