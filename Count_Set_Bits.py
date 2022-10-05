def countsetbits(n):
    count=0
    while(n):
        n&=(n-1)
        count+=1
    return count
n=int(input())
while(n):
    p=int(input())
    print(countsetbits(p))
    n-=1