import itertools

N,M = map(int,raw_input().split())
rel = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
  rel[i][i] = 1
for i in range(M):
  x,y = map(int,raw_input().split())
  x,y = x-1,y-1
  rel[x][y] = rel[y][x] = 1

def can_make_group(ptn):
  for p1 in ptn:
    for p2 in ptn:
      if rel[p1][p2] == 0: return False
  return True

def exist_ok_comb(n):
  arr = []
  for i in range(N):
    if sum(rel[i]) >= n: arr.append(i)
  if len(arr) < n:
    return False  
  for ptn in itertools.combinations(arr,n):
    if can_make_group(ptn):
      return True
  return False
  
def solve():
  ans = 1
  for n in range(2, N+1):
    if exist_ok_comb(n):
      ans = n
    else:
      break
  return ans    

print solve()