# example.py

# Define variables a and b
a = 15
b = 12

#Print the types of a and b
print("Type of a:", type(a))
print("Type of b:", type(b))

#Perform basic arithmetic operations and print the results
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

#Create a new variable c as integer division of a by b
c = a // b
print("Value of c (int):", c)
print("Type of c:", type(c))

#Convert c to float and print new value and type
c = float(c)
print("Value of c (float):", c)
print("Type of c:", type(c))

#String concatenation
message = "The result of a divided by b is: "
print(message + str(c))

#Comparison operators
print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)
