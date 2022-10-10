n=int(input())
while n:
    t=int(input())
    arr=list(map(int,input().split()))
    for i in range(t):
        if sum(arr[0:i])==sum(arr[i+1:]):
            print('YES')
            break
    else:
        print('NO')
    t-=1