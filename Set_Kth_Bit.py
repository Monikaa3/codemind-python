def setkthbit(p,k):
    return ((1<<k)|p)
p,k=map(int,input().split())
print(setkthbit(p,k))