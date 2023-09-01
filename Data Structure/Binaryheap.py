import heapq

a=[]
a1=[500,10,8,90,100,34]

heapq.heappush(a, 20)
heapq.heappush(a,30)
heapq.heappush(a,5)
heapq.heappush(a,7)

heapq.heapify(a1)
heapq.heappop(a1)

heapq.heappushpop(a1, 30)
heapq.heapreplace(a, 1)
print(a)
print(a1)

print(heapq.nlargest(2, a1))
print(heapq.nsmallest(2, a1))
