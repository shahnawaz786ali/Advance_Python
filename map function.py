a=[3,23,89,21,34]

def sqr(num):
    return(num*num)

#method 1
b=[]

for i in a:
    b.append(sqr(i))
    
print(b)
    
#method 2
    
print(list(map(sqr, a)))
    