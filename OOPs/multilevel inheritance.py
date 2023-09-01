class grandfather:
    grand_father=" "
    def __init__(self):
        self.grand_father

class father(grandfather):
    _father= " "
    def __init__(self):
        self._father
        super().__init__()

class son(father):
    _son=" "
    def __init__(self):
        self._son
        super().__init__()

    def display(self):
        print("Grandfather: ",self.grand_father)
        print("Father: ",self._father)
        print("Son: ",self._son)

obj2=son()

obj2.grand_father="salam"
obj2._father="laddoo"
obj2._son="sahil"

obj2.display()




 
