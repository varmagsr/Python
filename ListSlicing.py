import operator

numbers = [3, 5, 7, 9, 14]
print(numbers[0:5])
print(numbers[2])
print(numbers[-4])

#how to get last element in list
print(numbers[-1:][0])

#Get last item of a list using itemgetter
print(operator.itemgetter(-1)(numbers))

#Get last item of a list through Reverse Iterator
#reversed() function : It accepts a sequence and returns a Reverse Iterator of that sequence.
#next() function: It accepts an iterator and returns the next item from the iterator.
print(next(reversed(numbers), None))

#Get last item of a list by indexing
print(numbers[len(numbers)-1])

#Get last item of a list using list.pop()
print(numbers.pop())
print(numbers)
