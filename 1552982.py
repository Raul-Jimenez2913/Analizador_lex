deg,dis = map(int,raw_input().split())

DIR = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','N']
out1 = DIR[(deg*10 + 1125) // 2250]

WIND = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
p = int(dis*10.0/60 + 0.5)*1.0 / 10
#p = round(dis*1.0/60, 1)

out2 = 0
for i in range(len(WIND)):
  if WIND[i] >= p:
    out2 = i
    break
else:
  out2 = 12

if out2 == 0:
  out1 = 'C'

print out1,out2