class node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DoublyLL:
    def __init__(self):
        self.head=None

    def printlist(self):
        if self.head is None:
            print("empty linked list.")

        else:
            n=self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n=n.nref

    def printlist_reverse(self):
        if self.head is None:
            print("empty linked list.")

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref

            while n is not None:
                print(n.data)
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node=node(data)
            self.head=new_node

        else:
            print("Linked list is not empty.")

    
    def insert_beginning(self,data):
        new_node=node(data)

        if self.head is not None:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

        else:
            self.head=new_node


    def insert_end(self,data):
        new_node=node(data)

        n=self.head
        while n.nref is not None:
            n=n.nref

        new_node.nref=None
        new_node.pref=n
        n.nref=new_node

    def insert_before(self,data,x):
        
        if self.head is None:
            print("Empty linked list.")
            new_node=node()
            self.head=new_node
            return

        if self.head.data==x:
            new_node=node(data)
            new_node.nref=self.head
            self.head.pref=None
            self.head=new_node
            return

        n=self.head
        while n.nref is not None:
            if n.nref.data==x:
                break
            n=n.nref
        new_node=node(data)
        new_node.nref=n.nref
        new_node.pref=n
        n.nref=new_node


    def insert_after(self,data,x):
        n=self.head

        while n is not None:
            if n.data==x:
                break
            n=n.nref

        if n is None:
            print("Linked list is empty.")
            return

        else:
            new_node=node(data)
            new_node.nref=n.nref
            n.nref=new_node
            new_node.pref=n

    def del_begin(self):
        if self.head is None:
            print("Empty linked list.")
            return

        if self.head.nref is None:
            self.head=None
            print("Linked list is empty after deleting the node.")

        else:
            self.head=self.head.nref
            self.head.pref=None


    def del_end(self):
        if self.head is None:
            print("Empty linked list.")
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        n.pref.nref=None

    def del_by_value(self,x):

        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("element not present in given linked list.")
            return

        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return

        n=self.head
        while n.nref is not None:
            if n.nref.data==x:
                break
            n=n.nref

        n.nref=n.nref.nref
        n.nref.pref=n
       

n_llist=DoublyLL()
n_llist.insert_beginning(23)
n_llist.insert_end(90)
n_llist.insert_end(100)
n_llist.insert_end(500)
n_llist.insert_before(200,90)
n_llist.insert_before(180,23)
n_llist.insert_after(900,200)
n_llist.insert_before(250,180)
n_llist.insert_before(175, 200)
n_llist.insert_after(1000,900)
n_llist.insert_after(2500,250)
n_llist.del_begin()
n_llist.del_begin()
n_llist.del_end()
n_llist.del_end()
n_llist.del_by_value(180)

n_llist.printlist()



