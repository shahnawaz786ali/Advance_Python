class father:
    def __init__(self):
        print("I am father class.")
        
    def intro1(self):
        print("I am base1 class.")
        
class mother:
    def __init__(self):
        print("I am mother class.")
        
    def intro2(self):
        print("I am base2 class.")
        
class child(father,mother):
    def __init__(self):
        print("I am child class.")
        father.__init__(self)
        mother.__init__(self)
        
obj2=child()
obj2.intro1()
obj2.intro2()