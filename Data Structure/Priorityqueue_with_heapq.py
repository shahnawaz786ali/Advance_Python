import heapq as hq
import time
# list1=[(3,"sahil"),(1,"sagar"),(5,"abc"),(4,"xyz"),(2,"shahnawaz")]
# hq.heapify(list1)
# print(list1)

# print("The order of students is:")
# for i in list1:
#     print(i[0],":", i[1])

jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'),
         (4, 'task_5'), (3, 'task_3'), (1, 'task_8')]

interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')]

i,j=0,0

hq.heapify(jobs)
print("Jobs elements as per the rule of heapify: ", end=" ")
print(jobs)

while len(jobs)!=0:
    print("The", jobs[0][1], "with priority", jobs[0][0], "is in progress.", end="")

    for _ in range(5):
        print(".", end="")
        time.sleep(0.5)

    hq.heappop(jobs)

    if j< len(interrupts):
        hq.heappush(jobs,interrupts[j])
        print(interrupts[j])
        print()
        j=j+1

    # after adding interrupts
    print("Current jobs is:", jobs)
    print()

print("all interrupts and jobs completed.")
    
