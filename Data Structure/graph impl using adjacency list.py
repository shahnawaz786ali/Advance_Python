from collections import deque

def add_node(v):
    if v in graph:
        print(f"{v} already present in graph.")

    else:
        graph[v]=[]

def add_edge(v1,v2,weight):
    if v1 not in graph:
        print(f"{v1} not present in graph.")
    elif v2 not in graph:
        print(f"{v2} not present in graph.")

    else:
        list1=[v2, weight]
        list2=[v1, weight]

        graph[v1].append(list1)
        graph[v2].append(list2)

def del_node(v):
    if v not in graph:
        print(f"{v} not present in graph.")

    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]

            # for undirected unweighted graph
            # if v in list1:
            #     list1.remove(v)

            # for undirected weighted graph
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break

def del_edge(v1,v2,weight):
    if v1 not in graph:
        print(f"{v1} not prsent in graph.")
    elif v2 not in graph:
        print(f"{v2} not prsent in graph.")

    else:
        list1=[v2,weight]
        list2=[v1,weight]
        if list2 in graph[v2]:
            graph[v2].remove(list2)
            graph[v1].remove(list1)

def DFS(node,visited,graph):
    if node not in graph:
        print(f"{node} not present in graph.")
        return

    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i[0],visited,graph)

def DFSiterative(node,graph):
    visited=set()
    if node not in graph:
        print(f"{node} is not present in graph.")
        return
        
    stack = []
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i[0])

def BFS(node,graph):
    visited=set()
    if node not in graph:
        print(f"{node} not present in graph")
        
    else:
        queue=deque([node])
        while queue:
            current=queue.popleft()
            visited.add(current)
            for i in graph[current]:
                if i[0] not in visited:
                    queue.append(i[0])
    print(visited)

visited=set()
graph={}
add_node("A")
add_node("D")
add_node("C")
add_node("E")

add_edge("A","C",30)
add_edge("A","D",9)
add_edge("C", "E", 10)
add_edge("D", "E", 10)
print(graph)

# DFS("A",visited,graph)
DFSiterative("C", graph)
BFS("C",graph)
