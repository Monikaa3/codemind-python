n=int(input())
for i in range(0,n):
    t=int(input())
    a=[int(x) for x in input().split()]
    if t==1:
        print(0)
    else:
        v=[]
        for i in a:
            if i in range(1,1000000000,2):
                v.append(i)
        if len(v)==1:
            print(0)
        elif len(v)%2==0:
            print(int(len(v)/2))
        else:
            print(int((len(v)-1)/2))