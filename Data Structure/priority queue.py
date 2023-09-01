import queue

que=queue.PriorityQueue()

def add(item):
    que.put(item)
    print("Inserted element is: ", item)

def remove():
    x=que.get()
    print("Deleted element is: ", x)

while True:
    choice=int(input("Enter your choice: 1:add  2: delete  3:quit"))

    if choice==1:
        add(item=int(input()))

    elif choice==2:
        remove()

    elif choice== 3:
        quit()

    else:
        print("Enter correct choice:")
