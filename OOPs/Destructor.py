class animal:
    def lion(self):
        print("This method belongs to animal class.")

    #Destructor
    def __del__(self):
        print("I am deleting evrthing.")

obj=animal()
obj.lion()
del obj #if you don't want to keep this line than it's automatically collected by garbage collector so it's not compulsory