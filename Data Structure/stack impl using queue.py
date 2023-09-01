from queue import LifoQueue

stack=LifoQueue()

stack.put(20)
stack.put(90)
stack.put(34)
stack.put(10)

print(stack.get())
print(stack.get())
