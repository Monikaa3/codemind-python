p=int(input())
a=list(map(int,input().split()))
q=0
for i in a:
    if q<len(str(i)):
        q=len(str(i))
for i in a:
    if len(str(i))==q:
        print(i,end=' ')