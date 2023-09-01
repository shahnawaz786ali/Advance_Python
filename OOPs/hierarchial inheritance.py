class parent:
    name=" "
    def __init__(self):
        self.name

    def getname(self):
        print(self.name)

class child1(parent):
    age= ""
    def __init__(self):
        self.age
        super().__init__()

class child2(parent):
    colour=" "
    def __init__(self):
        self.colour
        super().__init__()

obj1=child1()
obj2=child2()

obj1.name="sahil"
obj2.name="rahul"

obj1.getname()
obj2.getname()
