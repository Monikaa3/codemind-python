s=input()
vowels='AEIOUaeiou'
c=0
constant='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
x=0
y=len(s)-1
while x<y:
    if((s[x] in vowels and s[y] in constant) or (s[x] in constant and s[y] in vowels)):
        c+=1
    x+=1
    y-=1
print(c)