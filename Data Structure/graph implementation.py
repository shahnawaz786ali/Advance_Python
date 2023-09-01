def add_node(data):
    global node_count
    if data in node:
        print(data, "is already present in node.")
    else:
        node_count += 1
        node.append(data)
        for n in graph:
            n.append(0)

        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(node1,node2, weight):
    if node1 not in node:
        print(f"{node1} is not present in nodes.")

    elif node2 not in node:
        print(f"{node2} is not present in nodes.")

    else:
        index1=node.index(node1)
        index2=node.index(node2)

        graph[index1][index2]=weight
        graph[index2][index1]=weight

def del_node(v):
    global node_count
    if v not in node:
        print(f"{v} is not present in graph.")

    else:
        index1=node.index(v)
        node_count -= 1
        node.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def del_edge(v1,v2):
    if v1 not in node:
        print(f"{v1} not present in graph.")

    elif v2 not in node:
        print(f"{v2} not present in graph.")

    else:
        index1=node.index(v1)
        index2=node.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

def matrix_display():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()

node=[]
graph=[]
node_count=0

print("Before adding node:")
print(node)
print(graph)

add_node(12)
add_node(100)
add_node(10)
add_edge(12,100,2)
add_edge(100,10,9)
print("After adding node:")
print(node)
print(graph)

# del_node(10)
del_edge(12,100)
print("After deleting node:")
print(node)
print(graph)
matrix_display()
