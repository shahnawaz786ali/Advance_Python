# Implementation of queue using two stack.

from collections import deque

class Queue:
    def __init__(self):
        self.s1=deque()
        self.s2=deque()

    def enque(self,key):
        while len(self.s1):
            self.s2.append(self.s1.pop())

        self.s1.append(key)

        while len(self.s2):
            self.s1.append(self.s2.pop())

    def deque(self):

        if not self.s1:
            print("Stack underflow")
            return

        return self.s1.pop()

a=[2,3,89,10,4]
que=Queue()

for i in a:
    que.enque(i)

print(que.deque())
print(que.deque())

