from functools import reduce

l=[2,3,4,5,6,7,0]

sum=lambda x,y : x+y

print(reduce(sum, l))