import queue

class priority:
    def add(self,que,item):
        que.put(item)
        print("Inserted elemeent is: ", item)

    def remove(self,que):
        x=que.get_nowait()
        print("deleted elemnet is: ", x)

que=queue.Queue()
a=priority()

a.add(que, "23")
a.add(que, "45")
a.add(que, "12")

a.remove(que)
a.remove(que)
a.remove(que)