#Water jug problem using BFS
#26-04-2023

j1=int(input('Enter the capacity of jug1: '))
j2=int(input('Enter the capacity of jug2: '))
g=int(input('Enter the amount of water to be measured: '))
x,y=0,0
visited=[(0,0)]
front,top=0,0
f=0

while front<=top:

    x,y=visited[front]

    if x==g or y==g:
        f=1
        break

    if x<j1 and (j1,y) not in visited:
        visited.append((j1,y))
        top+=1

    if y<j2 and (x,j2) not in visited:
        visited.append((x,j2))
        top+=1 

    if x>0 and (0,y) not in visited:
        visited.append((0,y))
        top+=1

    if y>0 and (x,0) not in visited:
        visited.append((x,0))
        top+=1

    if x+y<=j1 and y>0 and (x+y,0) not in visited:
        visited.append((x+y,0))
        top+=1

    if x+y<=j2 and x>0 and (0,x+y) not in visited:
        visited.append((0,x+y))
        top+=1

    if x+y>=j1 and y>0 and (j1,y-(j1-x)) not in visited:
        visited.append((j1,y-(j1-x)))
        top+=1

    if x+y>=j2 and x>0 and (x-(j2-y),j2) not in visited:
        visited.append((x-(j2-y),j2))
        top+=1

    front+=1


print('Water jug problem using BFS')
if f==1:
    visited=visited[:front+1]
    print(visited)
else:
    print('No solution')





#Water jug problem  DFS
#26-04-2023

def rule(x,y):

    visited.append((x,y))

    if x==g or y==g:
        return 1

    if x<j1 and (j1,y) not in visited:
        if rule(j1,y): return 1

    if y<j2 and (x,j2) not in visited:
        if rule(x,j2): return 1


    if x>0 and (0,y) not in visited:
        if rule(0,y): return 1


    if y>0 and (x,0) not in visited:
        if rule(x,0): return 1


    if x+y<=j1 and y>0 and (x+y,0) not in visited:
        if rule(x+y,0): return 1


    if x+y<=j2 and x>0 and (0,x+y) not in visited:
        if rule(0,x+y): return 1


    if x+y>=j1 and y>0 and (j1,y-(j1-x)) not in visited:
        if rule(j1,y-(j1-x)): return 1


    if x+y>=j2 and x>0 and (x-(j2-y),j2) not in visited:
        if rule(x-(j2-y),j2): return 1

    return 0


j1=int(input('Enter the capacity of jug1: '))
j2=int(input('Enter the capacity of jug2: '))
g=int(input('Enter the amount of water to be measured: '))
x,y=0,0
visited=[]
print('Water jug problem using DFS')
if rule(x,y):
    print(visited)
else:
    print('No solution')