'''A list contain the multiplication table of 7, Write a program to
to convert it to a vertical string 7
                                   ....
                                   ....
'''
list=str([7,14,21,28,35,42,49,56,63,70])

#method 1
for i in list:
    print(i)
    
#method 2
    
vertical="\n".join(list)
print(vertical)