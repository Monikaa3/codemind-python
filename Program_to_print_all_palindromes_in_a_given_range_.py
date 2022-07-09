x=int(input())
y=int(input())
for n in range(x,y+1):
    rev=0
    num=n
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(rev==num):
        print(rev,end=" ")