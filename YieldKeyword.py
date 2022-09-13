

#In Python inside a function instead of using return keyword, we can use yield keyword to return the value.
# But unlike return keyword, the yield keyword do not terminates the function,
# it just pauses the function by saving its current state like last executed line number,
# variables on stack and then it returns the yielded value. So, now next time when this function will be called,
# then it will start from the point it left off. If there is no value to yield and function reaches its end then StopIteration is raised.
# Otherwise if any another yield is encountered then it will again pause the function execution and returns the yielded value.

def primeNumbers():
    ''' A function that will yield 2 different values at different places'''
    print('step 1')
    # Yield a value
    yield 5

    print('step 2')
    # Yield a value
    yield 7


# Get a generator object
generator = primeNumbers()
# Get First element
num = next(generator)
print('First Element : ', num)


# Get Second element
num = next(generator)
print('Second Element : ', num)

#Similarly when we call the next() function third time then function primeNumbers() continues from the last paused location.
# Then it continues till it encounters any yield statement.
# As there is no more yield statement and function end is reached, therefore StopIteration is raised i.e.

# Get third element
num = next(generator)
print('Third Element : ', num)


#Referance: https://thispointer.com/python-use-of-yield-keyword-generators-explained-with-examples/