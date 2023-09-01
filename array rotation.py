def arrayrotation(arr,d,n):
    for i in range(d):
        arrayrotationbyone(arr,n)
    print(arr)

def arrayrotationbyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    
arr=[1,2,3,4,5]
arrayrotation(arr,3,5)