p=input().lower()
p=p.split(" ")
a=p[0]
x=''
for i in a:
        count = 0
        for j in range(1,len(p)):
            if i in p[j]:
                count+=1
        if count==len(p)-1:
            x+=i
if len(x)==0:
    print("-1")
else:
    print(x)