#Bidirectional Search

from collections import defaultdict
graph=defaultdict(list)

edges=eval(input('Enter edges: '))
for i in edges:
  graph[i[0]].append(i[1])
  graph[i[1]].append(i[0])

src=int(input('Enter initial state: '))
dest=int(input('Enter goal state: '))
visit_f=[src]
visit_b=[dest]
front_f,top_f,front_b,top_b=0,0,0,0

def bfs_f():
  if src==dest:
    return src
  global front_f,top_f

  while front_f<=top_f:
    s=visit_f[front_f]
    for i in graph[s]:
      if i not in visit_f:
        visit_f.append(i)
        top_f=top_f+1
        if i in visit_b:
          return i
        else:
          k=bfs_b()
          if k!=-1: return k

    front_f=front_f+1
  return -1

def bfs_b():
  global front_b,top_b

  while front_b<=top_b:
    s=visit_b[front_b]
    for i in graph[s]:
      if i not in visit_b:
        visit_b.append(i)
        top_b=top_b+1
        if i in visit_f:
          return i
        else:
          k=bfs_f()
          if k!=-1: return k

    front_b=front_b+1
  return -1

def remove(l,g):
  a=l.index(g)
  for i in range(a,0,-1):
    if [l[i],l[i-1]] not in edges and [l[i-1],l[i]] not in edges:
      l.remove(l[i-1])
  a=l.index(g)
  return a

g=bfs_f()
if g==-1:
  print('No intersection')
else:
  print('\nIntersection Node:',g)
  a=remove(visit_f,g)
  b=remove(visit_b,g)
  k=visit_f[:a]+visit_b[b::-1]
  print('Path :',k)

Enter edges: [[1,2],[1,5],[2,3],[2,4],[3,8],[3,9],[5,6],[5,7],[7,10],[7,11]]
Enter initial state: 1
Enter goal state: 9

Intersection Node: 2
Path : [1, 2, 3, 9]


