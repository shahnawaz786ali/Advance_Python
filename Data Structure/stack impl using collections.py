import collections

stack=collections.deque()

stack.append(10)
stack.append(90)
stack.append(70)

print(stack)

stack.pop()
stack.pop()
stack.pop()

print(stack)