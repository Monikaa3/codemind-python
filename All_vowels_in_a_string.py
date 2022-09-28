n=input()
a='aeiou'
b=0
c=[]
for i in n:
    if i in a:
        if i not in c:
            c.append(i)
if(len(c)==5):
    print(True)
else:
    print(False)