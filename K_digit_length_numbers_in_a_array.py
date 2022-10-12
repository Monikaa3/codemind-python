n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<0:
        i=(-1)*i
    s=str(i)
    if len(s)==k:
        c+=1
print(c)