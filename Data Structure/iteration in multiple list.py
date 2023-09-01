import itertools


list1=["1","2","3","5","9","10","4","90","12","11"]
list2=["1","45","2","3","5","9","10","4","90","11","12","67","45"]


for i,j in itertools.zip_longest(list1,list2):
    if (i==j) or (i==None):
        print("pass")
    