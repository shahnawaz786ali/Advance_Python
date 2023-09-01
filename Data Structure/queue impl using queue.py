from queue import Queue

que=Queue(maxsize=3)

def push(item):
    que.put(item)
    print("Inserted element is: ", item)


def pop():
    x=que.get()
    print("Deleted element is: ", x)
    
def display():
    print(que)

def isempty():
    if len(que)==0:
        print("Empty queue....")

def nowait():
    y=que.get_nowait()
    print("deeleted elemnet is: ", y)

while True:
    choice=int(input("Enter choice of operations: 1:push, 2:pop, 3:display, 4: quit, 5: empty 6:nowait"))

    if choice==1:
        push(item=input("item: "))

    elif choice==2:
        pop()
        
    elif choice==3:
        display()

    elif choice==4:
        nowait()

    elif choice==5:
        quit()

    elif choice==6:
        isempty()
    
    else:
        print("Enter correct input:")