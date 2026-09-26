# random numbers

#Q1. Import the random module and write a statement to generate a random integer
# between 1 and 6 inclusive (simulating a standard 6-sided die roll)

# import random
# roll = random.randint(1,6) #randint inclusive
# print(roll)

#Q2. Given a list colors = ["red", "green", "blue", "yellow"], use random.choice() to
# randomly pick and print one color.

# import random
# colors = ["red", "green", "blue", "yellow"]
# chosen_color = random.choice(colors)
# print(f"Randomly Chosen Color: {chosen_color}")

#Q3. Generate a random floating-point number between 0.0 and 1.0 using random.random(),
# and another float between 10.0 and 50.0 using random.uniform()
# import random
# floating = random.random()
# uni_float = random.uniform(10.0, 50.0)
# print(f"Random float between 0 to 1: {round(floating, 4)}")
# print(f"Uniform float between 10 to 50: {round(uni_float,2)}")

#Q4. Given a list of numbers cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use random.shuffle()
# to shuffle the list in-place and print the randomized list. Then use random.sample() to
# select 3 unique cards without modifying the original list

# import random
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(cards)
# print(cards)
#
# random_sample = random.sample(cards, 3)
# print(f"3 Unique cards: {random_sample}")

#Q5. Write a function generate_otp(length=6) that generates a randomized numeric
# One-Time Password (OTP) string of a given length (e.g., "482910"). Ensure that the returned
# OTP retains leading zeroes properly if generated.

import random

def generate_otp(length=6):
    digits = [str(random.randint(0, 9)) for _ in range(length)]
    return "".join(digits)

# Generate 6-digit OTP
otp_code = generate_otp(6)

print("Generated OTP:", otp_code)

