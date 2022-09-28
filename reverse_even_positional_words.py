m=input().split()
for i in range(len(m)):
    if i%2==0:
        print(m[i][::-1],end=' ')
    else:
        print(m[i],end=' ')