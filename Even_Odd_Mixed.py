n=int(input())
c=0
e=0
o=0
while n>0:
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    c+=1
    n=n//10
if c==e:
    print("Even")
elif c==o:
    print("Odd")
else:
    print("Mixed")