p=input().lower()
q=input().lower()
a=''
for i in p:
    if i in q and i not in a:
        a+=i
for i in q:
    if i in p and i not in a:
        a+=i
a=sorted(a)
a=str(a)
a=a.replace("[","")
a=a.replace("]","")
a=a.replace("","")
a=a.replace("'","")
a=a.replace(",","")
a=a.replace(" ","")
if len(a)==0:
    print("-1")
else:
    print(a)