N,K = map(int,raw_input().split())
R = map(float,raw_input().split())
R = sorted(R,reverse=True)
rslt = 0.0
for k in range(K):
	rslt = (rslt + R[K - k - 1]) / 2.0
print rslt