# CLASS ASSIGNMENT : 4
# DAY : MONDAY (2 TO 5 PM)
# ------------------------------
# Lesson: Control, Modules & Functions
# ------------------------------

# --- Control Flow ---
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

print("\n---------------------\n")

# Nested if
if x > 0:
    if x < 20:
        print("x is positive and less than 20")

print("\n---------------------\n")

# --- Loops ---
# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

print("\n---------------------\n")

# While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

print("\n---------------------\n")

# Break and Continue
for num in range(5):
    if num == 3:
        break  # exits loop
    if num == 1:
        continue  # skips the rest
    print("Number:", num)

print("\n---------------------\n")

# --- Functions ---
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def greet_user(name="Guest"):
    print(f"Welcome, {name}!")

print("\n---------------------\n")

print("Sum:", add(5, 3))
print("Is 4 even?", is_even(4))
greet_user("Sara")
greet_user()

print("\n---------------------\n")

# --- Modules ---
import math
import random

print("Random number:", random.randint(1, 10))
print("Square root of 49:", math.sqrt(49))


print("\n---------------------\n")

# ------------------------------
# Lesson: Exception Handling
# ------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid number")
except Exception as e:
    print("Other error:", e)
else:
    print("No errors occurred")
finally:
    print("End of exception block")

print("\n---------------------\n")

# Raise an Exception manually
def check_age(age):
    if age < 18:
        raise ValueError("Must be 18 or older")
    print("Access granted")

try:
    check_age(15)
except ValueError as ve:
    print(ve)

print("\n---------------------\n")


# ------------------------------
# Lesson: File Handling
# ------------------------------

# Writing to a File
with open("sample.txt", "w") as f:
    f.write("Python is fun!\n")
    f.write("This is another line.\n")

# Appending to a File
with open("sample.txt", "a") as f:
    f.write("Adding more content.\n")

# Reading Entire File
with open("sample.txt", "r") as f:
    print("Reading entire file:")
    print(f.read())

print("\n---------------------\n")

# Reading Line by Line
with open("sample.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())

print("\n---------------------\n")

# Reading Specific Lines
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("First line:", lines[0])

print("\n---------------------\n")

# ------------------------------
# Lesson : Math, DateTime, Calendar
# ------------------------------

# --- Math Module ---
import math
print("Pi:", math.pi)
print("Power of 2^3:", math.pow(2, 3))
print("Floor of 3.7:", math.floor(3.7))
print("Cosine of 0:", math.cos(0))

print("\n---------------------\n")

# --- DateTime Module ---
import datetime
now = datetime.datetime.now()
print("Now:", now)

print("\n---------------------\n")

# Create a specific date
d = datetime.date(2025, 4, 24)
print("Specific Date:", d)

print("\n---------------------\n")

# Date difference
d1 = datetime.date(2025, 1, 1)
d2 = datetime.date(2025, 4, 24)
diff = d2 - d1
print("Days difference:", diff.days)

print("\n---------------------\n")

# Time object
time = datetime.time(14, 30)
print("Custom time:", time)

print("\n---------------------\n")

# --- Calendar Module ---
import calendar
print("2025 Calendar:")
print(calendar.calendar(2025))

print("\n---------------------\n")

# Print month
print("Month calendar:")
print(calendar.month(2025, 4))

print("\n---------------------\n")

# Check leap year
print("Is 2024 a leap year?", calendar.isleap(2024))

print("\n---------------------\n")

# Set first weekday
calendar.setfirstweekday(calendar.SUNDAY)
print("Week header:", calendar.weekheader(3))

print("\n---------------------\n")
