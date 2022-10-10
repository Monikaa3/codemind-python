n,x=map(int,input().split())
a=list(map(int,input().split()))
t=0
c=0
for i in a:
    if i>x and t==1:
        break
    elif i>x:
        t+=1
    else:
        c+=1
print(c)