n=int(input())
k=list(map(int,input().split()))
e=[]
for i in k:
    s=str(i)
    l=len(s)
    e.append(l)
m=max(e)
for i in k:
    s=str(i)
    l=len(s)
    if l==m:
        print(i,end=' ')