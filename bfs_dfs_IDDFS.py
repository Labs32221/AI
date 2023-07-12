#12-04-2023
def dfs(graph,node):
    visited=[]
    stack=[]
    visited.append(node)
    stack.append(node)

    while stack:
        t=stack.pop()
        print(t, end=" ")

        for neighbor in graph[t]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

graph=eval(input('Enter graph: '))
s=int(input('Enter source: '))
dfs(graph,s)

Enter graph: {0:[1,2],1:[3],2:[3,4],3:[4],4:[0]}
Enter source: 0
0 2 4 3 1 

def bfs(graph,node):
    visited=[]
    queue=[]
    visited.append(node)
    queue.append(node)

    while queue:
        t=queue.pop(0)
        print(t, end=" ")

        for neighbor in graph[t]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph=eval(input('Enter graph: '))
s=int(input('Enter source: '))
bfs(graph,s)

Enter graph: {0:[1,2],1:[3],2:[3,4],3:[4],4:[0]}
Enter source: 0
0 1 2 3 4 


#Iterative Deepening Depth First Search
#14/06/2023
g=eval(input('Enter graph: '))
s=int(input('Enter source: '))
t=int(input('Enter target: '))
depth=int(input('Enter depth: '))

def DFS(d):
    visited=[s]
    stack=[s]
    check=[0]
    while stack:
        f=stack.pop()
        print(f,end=' ')
        p=check.pop()
        if f==t:
          print(' Target found within given depth')
          return 1
        if p+1>d:
          continue
        for neighbor in g[f]:
            if neighbor not in visited:
                check.append(p+1)
                visited.append(neighbor)
                stack.append(neighbor)
    return 0

def IDDFS():
  for i in range(depth+1):
    print('Depth',i,': ',end='')
    if DFS(i):
      break
    print()

IDDFS()
#{1:[2,5],2:[3,4],3:[8,9],5:[6,7],7:[10,11]}

Enter graph: {1:[2,5],2:[3,4],3:[8,9],5:[6,7],7:[10,11]}
Enter source: 1
Enter target: 6
Enter depth: 2
Depth 0 : 1 
Depth 1 : 1 5 2 
Depth 2 : 1 5 7 6  Target found within given depth