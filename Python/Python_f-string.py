# Python f-string
# Python f-string is the latest Python syntax to do string formatting.
# It is available since Python 3.6.
# Python f-strings provide a faster, more readable, more concise, 
# and less error prone way of formattings strings in Python.
#
# The f-strings have the f prefix and use {} brackets to evaluate values.
#
# Format specifiers for types, padding (e.g. 3.00), or aligning 
# are specified after the colon character (:) for instance:
# f"{price:.3}", where price is a variable name.

#%%
# An toy example for demonstration
name = "Peter"
age = 23
print("%s is %d years old" % (name, age))    # The oldest string formatting
print("{} is {} years old".format(name, age))  # The advance string formatting (since Python 3.0)
print(f"{name} is {age} years old")  # The f-strings string formating (since Python 3.6) 

#%%
# Python f-string expressions I
# Because f-strings are evaluated at runtime, 
# you can put any and all valid Python expressions in them.
bags = 3
apples_in_bag = 12

print(f"There are total of {bags * apples_in_bag} apples")

#%% Python f-string expression II
def to_lowercase(input):
    return input.lower()

name = "Amy Idle"
print(f"{to_lowercase(name)} is funny")

#%%
# Python f-string dictionaries
user = {"name": "John Doe", "occupation": "gardener"}

# The same result. (no matter what kind of chatacter ("" or '') you used.)
print(f"{user['name']} is a {user['occupation']}")
print(f'{user["name"]} is a {user["occupation"]}')

#%%
# Python f-string debug (Python 3.8)
import math

x = 0.8

print(f'{math.cos(x) = }') # Python 3.8
print(f"{math.sin(x) = }") # Python 3.8

print(f'{math.cos(x)}') 
# 0.6967067093471654

#%%
# Python multiline f-string
name = "John Doe"
age = 32
occupation = "gardener"

msg = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Occupation: {occupation}\n"
)

print(msg)

msg2 = f"Name: {name}\n" \
       f"Age: {age}\n" \
       f"Occupation: {occupation}\n"

print(msg2)

#%% 
# Python f-string calling function
def mymax(x, y):
    
    return x if x > y else y

a = 3
b = 4

print(f"Max of {a} and {b} is {mymax(a, b)}")

#%%
# Python f-string objects
# Python f-string accepts objects as well; the objects must 
# have either __str__() or __repr__() magic functions defined.
# The __str__() and repr__() methods deal with how objects are presented as strings,
# so you will need to make sure you include at least one of those methods in your
# class definition.
# By default, if both __str__() or __repr__() are definded, 
# f-strings will use __str__(), but you can make sure 
# they use __repr__() if you include the conversion flag !r. 
# However, if only one of the __str__() or __repr__() is defined, the flag !r
# has no effect.
# This example evaluates an object in the f-string.

class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    
    # The string returned by __repr__() is the official representation 
    # and should be unambiguous.
    def __repr__(self):
        return f"{self.name} is a {self.occupation}"
    
    # The string returned by __str__() is the informal string 
    # representation of an object and should be readable. 
    def __str__(self):
        return f"{self.name}"
    
u = User("John Doe", "gardener")

print(f"{u}")
print(f"{u!r}")

#%%
# Python f-string escaping characters
print(f"Python uses {{}} to evaluate variables in f-strings")
print(f"This was a \"great\" film")
print(f"{{70 + 4}} ")
# {70 + 4}
print(f"{{{70 + 4}}}")
# {74}
print(f"{{{{70 + 4}}}}")
# {{70 + 4}}

#%%
# Python f-string format datetime
import datetime

now = datetime.datetime.now()

print(f"{now:%Y-%m-%d %H:%M}")
# 2020-06-16 15:45

#%%
# Python f-string format floats (padding)
val = 12.3

print(f"{val:.2f}")
# 12.30
print(f"{val:.5f}")
# 12.30000

#%%
# Python f-string format width
# The width specifier sets the width of the value. 
# The value may be filled with spaces or other characters if the value is shorter than the specified width.
for x in range(1, 11):
    print(f"{x:03} {x*x:3} {x*x*x:4}")

# Output:
# 001   1    1
# 002   4    8
# 003   9   27
# 004  16   64
# 005  25  125
# 006  36  216
# 007  49  343
# 008  64  512
# 009  81  729
# 010 100 1000

#%%
# Python f-string justify string
# By default, the strings are justified to the left. 
# We can use the > character to justify the strings to the right. 
# The > character follows the colon character.

s1 = "a"
s2 = "ab"
s3 = "abc"
s4 = "abcd"

print(f"{s1:>10}")
print(f"{s2:>10}")
print(f"{s3:>10}")
print(f"{s4:>10}")

#%%
# Python f-string numeric notations
# Numbers can have various numeric notations, such as decadic or hexadecimal.
a = 300

# hexadecimal
print(f"{a:x}")
# 12c

# octal
print(f"{a:o}")
# 454

# scientific
print(f"{a:e}")
# 3.000000e+02