n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    i=str(i)
    s=len(i)
    l.append(s)
j=min(l)
c=l.count(j)
print(c)
    