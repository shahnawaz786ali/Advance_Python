'''
Write a program to find the maximum of number in a list
using reduce function
'''
from functools import reduce

l=[23,1,2,3,4,5,6,77768,9,28]

print(max(l))

#method 2

print(reduce(max, l))