def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if i>=b:
        if prime(i):
            c+=1
print(c)