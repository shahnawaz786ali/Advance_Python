class base:
    def __init__(self):
        self.name="sahil_sir"
        self._a="shahnawaz"  #protected variable
        self.__b="InfusingAI"  #private variable

class derived(base):
    def __init__(self):
        base.__init__(self)
        print("I am printing instance of base class.")
        print(self.name)
        print(self._a)

obj=derived()

print(obj.__b) # can't access outside the class as it is protected variable
