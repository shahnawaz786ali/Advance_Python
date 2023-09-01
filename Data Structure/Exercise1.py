#program to find all path from root to leaf.
class BT:
    def __init__(self,key):
        self.lchild=None
        self.rchild=None
        self.key=key

def printpath(root):
    path=[]
    printpathrec(root,path,0)

def printpathrec(root,path,pathlen):
    if root is None:
        print("tree is empty.")
        return

    if len(path)>pathlen:
        path[pathlen]=root.key

    else:
        path.append(root.key)

    pathlen=pathlen+1

    if root.lchild is None and root.rchild is None:
        printarray(path,pathlen)

    else:
        printpathrec(root.lchild,path,pathlen)
        printpathrec(root.rchild,path,pathlen)

def printarray(ints,len):
    for i in ints[0: len]:
        print(i, end=" ")
    print()

root=BT(5)
root.lchild=BT(4)
root.rchild=BT(10)
root.lchild.lchild=BT(3)
root.rchild.rchild=BT(15)
root.rchild.lchild=BT(2)

printpath(root)