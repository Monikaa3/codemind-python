from collections import deque
n=int(input())
a=list(map(int,input().split()))
p=int(input())
a=deque(a)
a.rotate(p)
a=list(a)
for i in a:
    print(i,end=' ')