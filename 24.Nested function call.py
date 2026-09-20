# nested function calls
#Q1.Given string input num_str = "  45.89  ", use nested function calls with print(), round(),
# float(), and str.strip() to strip whitespace, convert to float, round to 1 decimal place, and
# display the result in a single line

num_str = "  45.89  "

print(round(float(num_str.strip()),1))

#Q2. Write two functions: square(x) returning x^2, and double(x) returning 2x.
# Evaluate square(double(3)) in a single nested call and print the output

def square(x):
    return x ** 2
def double(x):
    return 2*x

print(square(double(3)))

#practice
def square(x):
    return x**2
def double(x):
    return x*2
result = square(double(3))

print(f"Result is: {result}")

#Q3. Use Python's built-in functions in a nested fashion to find the maximum value in a list
# of string numbers ["3", "15", "9", "2"] evaluated as integers rather than string
# alphabetical order

string_num = ["3", "15", "9", "2"]
print(max([int(x) for x in string_num]))

#alternative
string_num = ["3", "15", "9", "2"]
result = max(map(int, string_num))
print(result)

#Q4. Given a user input scenario with raw_input = "-18.75", write a single nested expression
# using abs(), round(), and float() to convert the string to a positive whole number integer

raw_input = "-18.75"
print(int(round(abs(float(raw_input)))))

#Q5. Create three functions:
# clean_text(text) -> removes leading/trailing spaces and converts to lowercase.
# count_words(text) -> splits text by spaces and returns the word count.
# format_output(count) -> returns formatted string "Total words: <count>".
# Combine all three into a single line of code using nested function calls on the input
# "   Python programming is versatile and powerful   ".

def clean_text(text):
    return text.strip().lower()
def count_word(text):
    return len(text.split())
def format_output(count):
    return f"Count words: {count}"

raw_data = "   Python programming is versatile and powerful   "
final_result = format_output(count_word(clean_text(raw_data)))
print(final_result)

#Practice
def clean_text(text):
    return text.strip().lower()
def count_words(text):
    return len(text.split())
def format_output(count):
    return f"Count words: {count}"
raw_data = "   Python programming is versatile and powerful   "
final_result = format_output(count_words(clean_text(raw_data)))
print(final_result)

