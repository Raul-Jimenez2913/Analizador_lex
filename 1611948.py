N,K = map(int,raw_input().split(' '))
R = map(float,raw_input().split(' '))
R = sorted(R,reverse=True)
C = 0
for k in range(K):
	C = (C + R[K - k - 1]) / 2.0

print C 
