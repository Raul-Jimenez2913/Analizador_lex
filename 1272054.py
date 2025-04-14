N = int(raw_input())
s = raw_input()
# 0: S, 1: W

def init():
    if s[0] == 'o':
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 0, 1, 1
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 0, 0, 0
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 1, 0, 1
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 1, 1, 0
        yield v
    else:
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 0, 0, 1
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 0, 1, 0
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 1, 1, 1
        yield v
        v = [-1 for i in range(N)]
        v[0], v[1], v[N-1] = 1, 0, 0
        yield v

def run():
    ok = False
    for v in init():
        ok = True
        for i in range(1, N):
            if s[i] == 'o':
                if v[i] == 0:
                    nv = v[i-1]
                else:
                    nv = 1-v[i-1]
            else:
                if v[i] == 0:
                    nv = 1-v[i-1]
                else:
                    nv = v[i-1]
            ni = (i+1) % N
            if (v[ni] > -1) and (v[ni] != nv):
                ok = False
                break
            v[ni] = nv 
        if ok:
            return ''.join(['S' if _ == 0 else 'W' for _ in v])
    return "-1"

print run()