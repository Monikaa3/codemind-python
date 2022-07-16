n=int(input())
lt=[]
p=0
s=0
for i in range(n):
    a=list(map(int,input().split()))
    lt.append(a)
for i in range(n):
    for j in range(n):
        if i==j:
            p+=lt[i][j]
        if i==(n-j)-1:
            s+=lt[i][j]
print("Principal Diagonal:{}".format(p))
print("Secondary Diagonal:{}".format(s))