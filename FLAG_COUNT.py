n=int(input())
p=0
r=2
for i in range(n):
    temp=p
    p=r
    r+=temp
print(p)