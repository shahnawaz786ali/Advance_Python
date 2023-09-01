'''
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the
i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a function that returns the number of times X appears as a value in
an N by N multiplication table.
'''
def matrix(N):
    for i in range(N):
        for j in range(N):
            a[i].append(((i+1)*(j+1)))
                           
N=int(input("Enter no. of rows and columns: "))
a=[]

for i in range(N):
    a.append([])           
matrix(N)
print(a)

X=int(input("Enter value to check: "))
count=0
for i in a:
    for j in i:
        if j==X:
            count=count+1
print(count)