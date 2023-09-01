class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        
    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        
        if self.key==data:
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
                
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    def search(self,data):
        if self.key==data:
            print("Element found")
            return
        
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
                
            else:
                print("Element not Found")
                
        else:
            if self.rchild:
                self.rchild.search(data)
                
            else:
                print("Element not found")
                
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.inorder()
            
        if self.rchild:
            self.rchild.inorder()
            
    def inorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key,end=" ")
        
        if self.rchild:
            self.rchild.preorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
            
        if self.rchild:
            self.rchild.postorder()
            
        print(self.key,end=" ")
        
    def delete(self,data,current_value):
        if self.key==None:
            print("Tree is empty.")
            return
        
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,current_value)
            else:
                print("Data not found.")
                
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,current_value)
                
            else:
                print("Data not found.")
                
        else:
            if self.lchild==None:
                temp=self.rchild
                if data==current_value:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rhild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            
            if self.rchild=None:
                temp=self.lchild
                if data==current_value:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            
            
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("Minimum node value is", current.key)
        
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("Maximum node value is", current.key)
        
            
bst=BST(10)
bst.insert(5)
bst.insert(8)
bst.insert(34)
bst.insert(12)
bst.postorder()
print()
bst.min_node()
bst.max_node()