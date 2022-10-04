n=input().lower()
m=input().lower()
a=''
for i in n:
    if i not in m and i not in a:
        a+=i
for i in m:
    if i not in n and i not in a:
        a+=i
a=a.replace(" ","")
print(len(a))