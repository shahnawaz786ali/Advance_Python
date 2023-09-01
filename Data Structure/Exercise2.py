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
                
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
            
        if self.rchild:
            self.rchild.preorder()
            
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        
        if self.rchild:
            self.rchild.inorder()
                
root=BST(40)

a=[12,98,45,23,9]

for i in a:
    root.insert(i)
root.preorder()