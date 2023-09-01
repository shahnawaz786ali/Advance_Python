class Parent:
    def __init__(self,name):
        self.name=name

    def getname(self):
        print(self.name)

class child(Parent):
    def __init__(self,name,age):
        self.age=age
        Parent.__init__(self,name)

    def getage(self):
        print(self.age)
        print(self.name)

obj=child("sahil",25)

obj.getage()