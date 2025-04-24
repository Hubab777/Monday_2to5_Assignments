# CLASS ASSIGNMENT : 3
# DAY : MONDAY (2 TO 5 PM)

# ========================================
# Lesson: Control Flow & Loops
# ========================================

# if-elif-else

# Diagram: if-elif-else
# 
#       +----------------+
#       |   Condition 1  |
#       +-------+--------+
#               |
#          True | False
#         +-----v----+     +----------------+
#         | Action 1 | --> | Condition 2    |
#         +----------+     +-------+--------+
#                                |
#                           True | False
#                          +-----v----+    +-----------+
#                          | Action 2 | -> | Else Block|
#                          +----------+    +-----------+

marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Needs Improvement")
    
print("\n-----------------------\n")

# Nested if
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
        
print("\n-----------------------\n")

# for loop with list
names = ["Ali", "Sara", "John"]
for name in names:
    print("Hello", name)
       
print("\n-----------------------\n")

# for loop with range and step
print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(i)
           
print("\n-----------------------\n")


# while loop with else
count = 0
while count < 3:
    print("Count is", count)
    count += 1
else:
    print("Finished counting")
       
print("\n-----------------------\n")

# break and continue in while loop
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    if num == 4:
        break
    print("Num:", num)
       
print("\n-----------------------\n")

# match-case (Python 3.10+)
day = "Friday"
match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("End of week")
    case _:
        print("Some other day")
       
print("\n-----------------------\n")

# ========================================
# Lesson: Lists, Tuples & Dictionary
# ========================================

# Lists
students = ["Ali", "Fatima", "Ahmed"]
students.insert(1, "Sara")
students.remove("Ahmed")
print("Students:", students)
print("Number of students:", len(students))
print("Last student:", students[-1])
       
print("\n-----------------------\n")

# List methods
students.append("Zara")
students.sort()
students.reverse()
print("Updated Students:", students)
print("Index of Zara:", students.index("Zara"))
       
print("\n-----------------------\n")

# List comprehension
squares = [x*x for x in range(1, 6)]
print("Squares:", squares)
       
print("\n-----------------------\n")

# Tuples
dimensions = (1920, 1080)
print("Width:", dimensions[0])
print("Height:", dimensions[1])

# Tuple methods
tup = (1, 2, 2, 3)
print("Count of 2:", tup.count(2))
print("Index of 3:", tup.index(3))
       
print("\n-----------------------\n")

# Nested tuple
person = ("John", 30, ("Engineer", "Developer"))
print("Job 1:", person[2][0])
       
print("\n-----------------------\n")

# Dictionaries
person = {
    "name": "Zulaikha",
    "age": 25,
    "hobbies": ["reading", "traveling"]
}
print("Name:", person.get("name"))
print("Hobbies:", person["hobbies"])
       
print("\n-----------------------\n")

# Add new key-value pair
person["email"] = "zulaikha@example.com"

# Dictionary methods
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())
person.update({"age": 26})
print("Updated Dictionary:", person)
person.pop("email")
       
print("\n-----------------------\n")

# Loop over keys
for key in person:
    print(key, "=", person[key])
       
print("\n-----------------------\n")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares_dict)
       
print("\n-----------------------\n")

# ========================================
# LESSON: Set & Frozenset
# ========================================

# Set basics
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.update(["black", "white"])
print("Colors:", colors)
       
print("\n-----------------------\n")

# Remove elements
colors.discard("green")
print("After removal:", colors)
       
print("\n-----------------------\n")

# Set methods and operations
x = {1, 2, 3}
y = {3, 4, 5}
print("Union:", x.union(y))
print("Intersection:", x.intersection(y))
print("Difference (x - y):", x.difference(y))
print("Symmetric Difference:", x.symmetric_difference(y))
       
print("\n-----------------------\n")

# Set properties
print("Is x a subset of y?", x.issubset(y))
print("Is x a superset of y?", x.issuperset(y))
print("Is x and y disjoint?", x.isdisjoint(y))
       
print("\n-----------------------\n")

# Frozenset examples
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print("Frozenset Intersection:", fs1 & fs2)
print("Frozenset Union:", fs1 | fs2)
       
print("\n-----------------------\n")

# Frozensets are immutable
# fs1.add(6)  # ❌ Error: frozensets are immutable

# ========================================
# CONCEPTS:
# ========================================

# List vs Tuple vs Dictionary:
# List      -> [1, 2, 3]       (Mutable, Ordered)
# Tuple     -> (1, 2, 3)       (Immutable, Ordered)
# Dictionary -> {"a": 1}      (Key-value, Mutable)

# Set Diagram:
# A = {1, 2, 3}
# B = {3, 4, 5}
# A | B = {1,2,3,4,5} (Union)
# A & B = {3} (Intersection)
# A - B = {1,2} (Difference)
# A ^ B = {1,2,4,5} (Symmetric Difference)

# Dictionary Keys/Values:
# person = {"name": "Ali", "age": 22}
# keys() -> ["name", "age"]
# values() -> ["Ali", 22]
# items() -> [("name", "Ali"), ("age", 22)]
