# queue implementation using single stack
from collections import deque

class Queue:
    def __init__(self):
        self.s=deque()

    def enque(self,data):
        self.s.append(data)

    def deque(self):
        if not self.s:
            print("stack underflow")
            return

        pop=self.s.pop()

        if not self.s:
            return pop

        item=self.deque()

        self.s.append(pop)
        return item

a=[2,4,7,9,12]
que=Queue()

for i in a:
    que.enque(i)

print(que.deque())
print(que.deque())