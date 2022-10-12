def count(s):
    s=str(s)
    c=0
    for i in s:
        c+=1
    return c
n=int(input())
k=list(map(int,input().split()))
for i in k:
    if i<0:
        i=(-1)*i
    s=count(i)
    print(s,end=' ')