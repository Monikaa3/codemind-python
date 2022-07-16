n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
l=[]
for i in range(n-1,0,-2):
    l.append(a[i-1])
    l.append(a[i])
    if len(l)==n:
        break
if len(a)%2!=0:
    l.append(a[0])
for i in l:
    print(i,end=' ')
        
