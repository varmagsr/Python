

#Other programming languages like C++ and Java have ternary operators, which are useful to make decision making in a single line.
#Python does not have a ternary operator. But in python, we can use the if-else in a single line,
#and it will give the same effect as the ternary operator.

#Example 1
x = 18
result = 'High' if x > 10 else 'Low'
print(result)

#Example 2
x = 20
result = 10 + 10 if x > 100 else 0
print(result)

#Example 3
x = 20
result = 10 + (10 if x > 100 else 0)
print(result)