from scipy.sparse import csr_matrix as mat
from scipy.sparse.csgraph import dijkstra as sp
from numpy import array, inf
N, M, T = map(int, raw_input().split())
A = map(int, raw_input().split())
E = array([map(int, raw_input().split()) for _ in range(M)])
fr, to, w = E[:, 0]-1, E[:, 1]-1, E[:, 2]
g, rg = mat((w, (fr, to)), shape=(N, N)), mat((w, (to, fr)), shape=(N, N))
d, rd = sp(g, indices=0), sp(rg, indices=0)
print(max(A[i] * (T - int(d[i] + rd[i])) for i in xrange(N) if max(d[i], rd[i]) < inf))