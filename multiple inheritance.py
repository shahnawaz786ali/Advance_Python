class father:
    def __init__(self, name,age):
        self.name=name
        self.age=age

class mother:
    def __init__(self,name1,age1):
        self.name1=name1
        self.age1=age1

class son(father,mother):
    def __init__(self, name, age,name1,age1):
        father.__init__(self,name, age)
        mother.__init__(self,name1,age1)

    def display(self):
        print(self.name)
        print(self.age)
        print(self.name1)
        print(self.age1)

obj=son("sahil", 25,"sad", 20)

obj.display()