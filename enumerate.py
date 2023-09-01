list=[78,54,23,00,34]

for index,item in enumerate(list):
    print(index,item)
    
    
#print 2nd and last element.
    
for index,item in enumerate(list):
    if index == 2 or index == 4:
        print(f'The {index + 1}rd element is {item}')