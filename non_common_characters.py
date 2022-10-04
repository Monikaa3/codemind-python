n=input().lower()
m=input().lower()
p=''
for i in n:
    if i not in m and i not in p:
        p+=i
for i in m:
    if i not in n and i not in p:
        p+=i
p=p.replace(" ","")
for i in sorted(p):
    print(i,end='')