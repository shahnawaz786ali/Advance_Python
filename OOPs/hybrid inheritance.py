class num1:
    def __init__(self,num3):
        self.num3=num3

class num2:
    def __init__(self,num4):
        self.num4=num4

# multiple inheritance
class num1_num2(num1,num2):
    def __init__(self,num3,num4):
        num1.__init__(self,num3)
        num2.__init__(self,num4)

    def add(self):
        a=self.num3 + self.num4
        print(a)

# multilevel inheritance
class cross(num1_num2):
    def __init__(self,num3,num4,num5):
        self.num5=num5
        num1_num2.__init__(self, num3,num4)

    def mul(self):
        return self.num3 * self.num4 * self.num5


obj=cross(3,4,2)
print(obj.mul())