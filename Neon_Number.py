num=int(input())
sqr=num*num
sumofDigit=0
while sqr>0:
    sumofDigit=sumofDigit+sqr%10
    sqr=sqr//10
if(num==sumofDigit):
    print("Neon Number")
else:
    print("Not Neon Number")
