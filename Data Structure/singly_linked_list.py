class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class L_List:
    def __init__(self):
        self.head=None

    def print_LL(self):
        n=self.head
        if n == None:
            print("Linked list is empty.")

        else:
            while n is not None:
                print(n.data, "--->", end=" ")
                n=n.ref

    # def reverse_LL(self):
    #     n=self.head
    #     a=[]
    #     while n is not None:
    #         a.append(n.data)
    #         n=n.ref
    #     for i in range(len(a)):
    #         print(a.pop(), end="--->")

    def add_beginning(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    # add between
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Linked kist is empty.")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    # add between
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref

        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node


    def add_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while (last.ref):
            last=last.ref   
        last.ref=new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty.")

        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")

        elif self.head.ref is None:
            self.head=None

        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref

            n.ref=None

    def del_by_value(self,x):
        if self.head is None:
            print("LList is empty.")
            return
        
        if self.head.data==x:
            self.head=self.head.ref
            return

        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref

        if n.ref is None:
            print("Node is empty.")

        else:
            n.ref=n.ref.ref     
        

n_list=L_List()
n_list.add_beginning("sahil")
n_list.add_beginning("sagar")
n_list.add_end(890)
n_list.add_beginning(23)
n_list.add_end("love")
n_list.add_after(200,890)
n_list.add_before("shahnawaz","sagar")
n_list.del_by_value(23)
n_list.delete_end()
n_list.print_LL()