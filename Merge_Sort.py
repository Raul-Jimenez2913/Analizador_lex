N = int(input())
time = []
for _ in range(N):
    _time = list(map(int, input().split('-')))
    time.append(_time)

def marume(t, d):
    if d == 'sita':
        while t%5:
            t -= 1
        return t
    else:
        while t%5:
            t += 1
        if t%100 == 60:
            t = t + 100 - 60
        return t

def merge(t1, t2):
    if (t1[0] - t2[1])*(t1[1] - t2[0]) <= 0:
        return [min(t1[0], t2[0]), max(t1[1], t2[1])]
    else:
        return False

def t2i(t):
    return int((t % 100 + t // 100 * 60) / 5)

def i2t(i):
    return (i*5//60) * 100 + i*5%60

time = [[marume(t[0], 'sita'), marume(t[1], 'ue')] for t in time]
index = [0 for i in range(290)]
for t in time:
    index[t2i(t[0])] += 1
    index[t2i(t[1])] -= 1

cumsum = 0
for i, ind in enumerate(index):
    cumsum += ind
    index[i] = cumsum

pre = 0
ans = []
for i, ind in enumerate(index):
    if pre < 1:
        if ind >= 1:
            ans.append(i)
    else:
        if ind < 1:
            ans.append(i)
    pre = ind

for i in range(len(ans)//2):
    print("{0:04d}-{1:04d}".format(i2t(ans[2*i]), i2t(ans[2*i+1])))
