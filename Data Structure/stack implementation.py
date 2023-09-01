import collections

stack=collections.deque(maxlen=3)

def push(a,item):
    a.append(item)
    print("adding elemnt: ",item)

def pop(a):
    x=a.pop()
    print("Deleting elemnt: ", x)

def display():
    print("Updated stack is: ", stack)

push(stack, "20")
push(stack, 30)
push(stack,"sahil")

stack.pop()
stack.pop()
stack.pop()

display()


