s=input().split(" ")
v='aeiouAEIOU'
a=0
for i in s:
    x=0
    y=len(i)-1
    while x<y:
        if((i[x] in v and i[y] not in v) or (i[x] not in v and i[y] in v)):
            a+=1
        x+=1
        y-=1
print(a)
            