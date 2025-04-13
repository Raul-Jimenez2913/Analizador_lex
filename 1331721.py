N = int(raw_input())
T = [False]*481
for i in range(N):
    S,E = raw_input().split("-")
    S = int(S[:2]) * 60 + int(S[2:])
    E = int(E[:2]) * 60 + int(E[2:])
    S /= 5
    E = (E-1)/5
    for j in range(S,E+1):
        T[j] = True

ss = ""
state = False
for i in range(481):
    if state != T[i]:
        j = i*5
        if state:
            print ss + "-" + ("%02d%02d"%(j/60,j%60))
            ss = ""
        else:
            ss = "%02d%02d"%(j/60,j%60)
        state = T[i]

if ss != "":
    print ss + "-2400"