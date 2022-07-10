num=int(input())
square=num*num
flag=0
while(num>0):
    rem=num%10
    if(rem!=square%10):
        print("Not an Automorphic Number")
        flag=1
        break
    num=num//10
    square=square//10
if(flag==0):
    print("Automorphic Number")