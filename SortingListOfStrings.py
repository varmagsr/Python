
# By Alphabetical Order
# By Reverse Alphabetical Order
# By String Length
# By Numeric Order


# Sort a List of strings in Alphabetical Order
lt = ['hi', 'hello', 'at', 'this', 'there', 'from']
lt.sort()  # Note: sort() don't return any value, it just updateds existing list with sorted list.
print(lt)

#Sort a List of strings alphabetically in Reverse Order
lt = ['hi', 'hello', 'at', 'this', 'there', 'from']
lt.sort(reverse=True)  # Note: sort() don't return any value, it just updateds existing list with sorted list.
print(lt)

#Sort a List of string by Length
lt = ['hi', 'hello', 'at', 'this', 'there', 'from']
lt.sort(key=len)  # Note: sort() don't return any value, it just updateds existing list with sorted list.
print(lt)

#Sort a List of string by Numeric Order
lN = ['55' , '101', '152', '98', '233', '40', '67']
lN.sort(key=int)
print(lN)


#Sorting a list of strings by Numerically in descending Order
lN = ['55' , '101', '152', '98', '233', '40', '67']
lN.sort(reverse=True, key=int)
print(lN)