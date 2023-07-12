# 9.	Implement Crypt arithmetic problems.

import itertools

def number(n,d):
  t=0
  for i in n:
    t=d[i]+(t*10)
  return t

def test(l,s,d):
  sum=0
  for i in l:
    sum=sum+number(i,d)
  if sum==number(s,d):
    return 1
  return 0

def check(d):
  for i in d.keys():
    if i in c and d[i]==0:
      return 1
  return 0

l=input('Enter list of strings: ').split()
s=input('Enter output string: ')

c=[]
for i in l:
  c.append(i[0])
c.append(s[0])

p=list(set(''.join(l)+s))
q=len(p)

k=list(itertools.permutations(range(0,10),q))

d={}
f=0
for i in k:
  for j in range(q):
    d[p[j]]=i[j]
  if check(d):
    continue
  if test(l,s,d) == 1:
    f=1
    print(d)
    print('Solution found')
    break

if f==0: print('No solution found')