import math
import os

print("--- Pip & Modules ---")
print("Square root of 25:", math.sqrt(25))
print("Current Working Directory:", os.getcwd())import math


# 1. Modules & Import concept
print("--- 1. Python Modules Demo ---")
radius = 5
area = math.pi * (radius ** 2)
print(f"Area of circle with radius {radius} is: {area:.2f}")

# 2. Pip & Fun feature (Using random module)
print("\n--- 2. Pip & External Packages Concept ---")
# Note: External modules ke liye terminal mein 'pip install module_name' likhte hain.
# Jaise yahan humne built-in 'random' use kiya hai:
lucky_roll = random.randint(1, 6)
print(f"Aapne dice roll kiya aur aaya: {lucky_roll} 🎲")

if lucky_roll == 6:
    print("Wah! Jackpot lag gaya! 😎")
else:
    print("Koi baat nahi, agli baar 6 aayega! 🚀")
