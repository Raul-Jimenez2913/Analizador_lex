N,M=map(int,raw_input().split())

S=[]
for i in range(N):
    S.append(set([i]))
for i in range(M):
    x,y=map(int,raw_input().split())
    x-=1
    y-=1
    S[x].add(y)
    S[y].add(x)

def complete(l):
    for i in l:
        for j in l:
            if j not in S[i]:
                return False
    return True

maxi = 1
for i in range(1<<N):
    j = 1
    c = 0
    s = set()
    while j <= i:
        if i & j > 0:
            s.add(c)
        j<<=1
        c+=1
    if len(s) <= maxi:
        continue
    if complete(s):
        maxi = len(s)

print maxi