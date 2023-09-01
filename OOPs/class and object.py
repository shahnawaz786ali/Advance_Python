class office:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def value(self):
        print(self.name)
        print(self.age)
        
obj=office("sahil",25)
obj1=office("sad",29)

obj1.name="rahul"

print(obj1.name)
print(obj1.age)





