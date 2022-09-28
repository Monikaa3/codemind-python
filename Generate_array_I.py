n=int(input())
p=list(map(int,input().split()))
res=[]
for i in range(0,n,2):
    while p[i+1]:
        res.append(p[i])
        p[i+1]-=1
print(*res)
