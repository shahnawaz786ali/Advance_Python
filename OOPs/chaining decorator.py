from turtle import *

def cir(func):
    print("I will make circle.")
    def inner1():
        circle(50)
    return inner1()

def hex(func):
    print("I will make hexagon and call square function.")
    def inner2():
        for i in range(6):
            fd(100)
            rt(60)
        return func()
    return inner2()

def square():
    print("i am actual function.")
    for i in range(4):
        fd(100)
        rt(90)

a=cir(hex(square))
print(a)
mainloop()
