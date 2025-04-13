m = input() / 1000.0
if m < 0.1:
    print "00"
elif m <= 5:
    print "%02d" % int(10*m)
elif m <= 30:
    print "%02d" % int(m+50)
elif m <= 70:
    print "%02d" % int((m-30)/5 + 80)
else:
    print "89"