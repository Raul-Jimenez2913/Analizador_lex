m = input()
M = m /1000.000

if M < 0.1:
  print "00"
elif M <= 5:
  if M < 1:
    N=int(M*10)
    print "0"+str(N)
  else:
    print int(M*10)
elif M <= 30:
  print int(M+50)
elif M <= 70:
  print int((M - 30)/5 + 80)
else:
  print "89"
