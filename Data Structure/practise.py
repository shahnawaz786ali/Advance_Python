# print all elements in sorted order from row and column wise sorted matrix

import heapq as hq

mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

print("Elements in sorted order are:", end="")

for i in mat:
    for j in i:
        print(j, end=" ")
