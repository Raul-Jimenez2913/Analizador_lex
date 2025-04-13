W = raw_input()
ar = []
for c in W:
  if c in ('a','i','u','e','o'): continue
  ar.append(c)
print ''.join(ar)