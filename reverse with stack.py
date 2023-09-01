stack=[]

for i in range(1,11):
    stack.append(i)

print(stack)
stack1=[]
num=1
while num <= 10:
    if len(stack)==0:
        print("Stack is empty.")
    stack1.append(stack.pop())
    num += 1
    
print(stack1)


# for string
stack2=[]

for i in "InfusingAI":
    stack2.append(i)

print(stack2)
stack3=[]
num=1
while num <= 10:
    if len(stack2)==0:
        print("Stack is empty.")
    stack3.append(stack2.pop())
    num += 1
    
print(stack3)

    
