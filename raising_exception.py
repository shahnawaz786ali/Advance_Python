def sum(num):
    try:
        return num + 1
    
    except:
        raise ValueError("This is not good.")
    
    
a=sum(12)
print(a)


# program to display a/b where a and b are integers , if b=0
#display infinite by ZeroDivisionError

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

try:
    print(a/b)
    
except:
    print("Infinity")
    