'''
Write a program to filter a list of number which is divisible
by 5.
'''

l=[23,89,90,12,25,70]

div=lambda num: num % 5==0

print(list(filter(div, l)))