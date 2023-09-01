num=int(input("Enter ur number:"))
list=[i*num for i in range(1,11)]

print(list)

with open('file.txt', "a") as f:
    f.write(str(list))
    f.write('\n')