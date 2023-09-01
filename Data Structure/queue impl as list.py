que=[]

def push(item):
    que.append(item)
    print("Inserted element is: ", item)

def pop():
    x=que.pop(0)
    print("Deleted element is: ", x)

def isempty():
    if len(que)==0:
        print("Empty queue....")

def display():
    print(que)

while True:
    choice=int(input("Enter choice of operations: 1:push, 2:pop, 3:display, 4: quit, 5: empty :" ))

    if choice==1:
        push(item=input("item: "))

    elif choice==2:
        pop()

    elif choice==3:
        display()

    elif choice==4:
        quit()

    elif choice==5:
        isempty()
    
    else:
        print("Enter correct input:")