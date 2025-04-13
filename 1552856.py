xa,ya,xb,yb,xc,yc = map(int,raw_input().split())
a = xb-xa
b = yb-ya
c = xc-xa
d = yc-ya
print abs(a*d - b*c)*1.0 / 2