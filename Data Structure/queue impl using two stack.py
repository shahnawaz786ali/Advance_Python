# Implementation of queue using two stack.
#Second method

from collections import deque


class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enque(self, key):
        self.s1.append(key)

    def deque(self):

        if not self.s1 and not self.s2:
            print("Stack underflow")
            return

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()


a = [2, 3, 89, 10, 4]
que = Queue()

for i in a:
    que.enque(i)

print(que.deque())
print(que.deque())
