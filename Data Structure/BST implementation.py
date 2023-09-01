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
            if self.rchild==None:
                self.rchild=BST(data)
            else:
                self.rchild.insert(data)
                
    def search(self,data):
        if self.key==data:
            print("data is found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
                
            else:
                print("data not found.")
                
        else:
            if self.rchild:
                self.rchild.search(data)
                
            else:
                print("data not found.")
                
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
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()   
        print(self.key,end=" ")
        
    def delete(self,data,current_value):
        if self.key is None:
            print("Tree is empty.")
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,current_value)
            else:
                print("Data is not found.")
                
        elif self.key < data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,current_value)
            else:
                print("Data is not found.")
                
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==current_value:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            
            if self.rchild is None:
                temp=self.lchild
                if data==current_value:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            
            node=self.rchild
            while self.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,current_value)
        return self
    
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("Node with minumum value is:", current.key)
        
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("Node with maximun value is:", current.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild) 

root=BST(20)

list1=[12,11,10,5,9]

for i in list1:
    root.insert(i) 

print("preorder")
root.preorder()
print()

if count(root)>1:
    root.delete(20,root.key)
else:
    print("Cant't perform deletion operation...")
    
print("after deletion..")
root.preorder()

print()
root.min_node()
root.max_node()