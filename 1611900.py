inPut = map(float,raw_input().split(' '))
a = inPut[0:2]
b = inPut[2:4]
c = inPut[4:6]

for i in range(2):
	b[i] -= a[i]
	c[i] -= a[i]

menseki = abs(b[0]*c[1] - b[1]*c[0]) / 2.0
print menseki