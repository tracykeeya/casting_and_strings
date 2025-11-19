#Practice Questions

#1. What is the type of the result when you add an integer 7 to a float 2.3?
num_int = 7
num_float = 2.3
results = num_int + num_float
print(results)

print(type(results))

#2. Try this code and predict the output:
x = 4
y = 5.0
z = x + y
print(z, type(z))

# Convert String to Integer
#1. Convert the string "250" into an integer and subtract 50. What is the result?
num_str = "250"
num_int = int(num_str)
print(num_int - 50)
print(type(num_int))


#2. What happens if you try int("hello")? Explain.
# print(int("hello"))
# It raises a ValueError because "hello" cannot be converted to an integer.

#Convert Integer to Float
#1. Convert the integer 12 to a float and multiply by 3.5. What is the result?
x = 12
y = float(x)
print(y *3.5)

#2. Convert 0 to a float. What is the type and value?
m = float(0)
print(m)
print(type(m))

# Convert Float to Integer
#Convert 7.89 into an integer. What is the result?
float = 7.89
nt = int(float)
print(nt)
print(type(nt))

#2. If x = 12.0, convert it to int. Does the value change?
x = 12.0
y = int(x)
print(y)
#yes it changes from float to int but the value remains the same.

#Convert Number to String
#Convert the integer 100 to a string and concatenate it with " apples".
x = 100
number = str((x)) + "apples"
print(number)
# 2. What is the result of:
num = 45
print("Number: " + str(num))
# Number: 45

#Convert String to Float
# 1. Convert "7.2" to a float and add 2.8. What is the result?

# x = "7.2"
# n = float(x)
# print(n + 2.8)

# 2. Convert "10" to float and multiply by 3. What is the output?
# y = "10"
# m = float(y)
# print(m *3)


# Convert to Boolean

print(bool(0)) # False
print(bool(1)) # True
print(bool("")) # False
print(bool("Hi")) 

# What is the boolean value of [] and [0]?
print(bool([]))# False
print(bool([0]))#True

# 2. Predict the result:
x = ""
y = bool(x)
print(y) # False

# 3. Convert 5 to boolean. What is the result?
n = 5
m = bool(n)
print(m) # True

#0r
print(bool([5]))

# Using the table, convert 3.7 to integer and float. Show types.
# Expression   Output   Type
# int(3.7)       3       int
# float(3)       3.0     float

# 2. Convert "0" to boolean. What is the result?
print(bool(0)) # false

# or
x = 0
y = bool(x)
print(y)
# 3. Convert False to integer and float. Show outputs.
x = False
y = int(x)
print(y)

# x = False
# y = float(x)
# print(y)


# Challenge Practice Questions
# 1. Ask the user for two numbers as input, convert them to integers, add them, and 
# display the result.
# 2. Ask the user for their age as a string input, convert to integer, and print a message:
m = "23"
n = int(m)
print(n)
print("You are" + str(n) + "years old")

# You are <age> years old
# 3. Convert a float 12.75 to integer, string, and boolean. Print the value and type for 
# each conversion.

p = 12.75
#Integer
y = int(p)
print(y)
print(type(y))
#string
c = str(p)
print(c)
print(type(c))

k = bool(p)
print(k)
print(type(k))