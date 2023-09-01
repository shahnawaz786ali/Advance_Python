class base:
    def name(self):
        print("My name is base class.")

    def intro(self):
        print("welcome to method overriding.")

class child1(base):
    def name(self):
        print("My name is class1.")

class child2(base):
    def name(self):
        print("My name is class2.")

obj1=child1()
obj2=child2()
obj=base()

obj.intro()
obj.name()

obj1.intro()
obj1.name()

obj2.intro()
obj2.name()