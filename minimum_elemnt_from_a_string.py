p=list(map(str,input().split()))
p=p[len(p)-1]
q=min(p)
if p.count(q.lower())!=0:
    print(q.lower())
else:
    print(q)