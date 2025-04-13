N = input()
mem = [0 for i in range(24*12)]

for i in range(N):
  s = raw_input()
  start_h = int(s[0:2])
  start_m = int(s[2:4])
  end_h = int(s[5:7])
  end_m = int(s[7:9])
  si = (start_h * 60 + start_m) // 5
  ei = (end_h * 60 + end_m - 1) // 5
  for j in range(si,ei+1):
    mem[j] = 1

#for h in range(24):
#  print mem[h*12:(h+1)*12]

prev = 0
start = -1
for i in range(len(mem)):
  if prev == 0 and mem[i] == 1:
    start = i
    prev = 1
  elif prev == 1 and mem[i] == 0:
    start_h = start // 12
    start_m = (start % 12) * 5
    end_h = i // 12
    end_m = (i % 12) * 5
    print "{0:02d}{1:02d}-{2:02d}{3:02d}".format(start_h,start_m,end_h,end_m)
    prev = 0
else:
  if prev == 1:
    start_h = start // 12
    start_m = (start % 12) * 5
    print "{0:02d}{1:02d}-2400".format(start_h,start_m)