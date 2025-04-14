import heapq
import math


def solve(xs, ys, xt, yt, N, a):
    a.insert(0, [xs, ys, 0])

    a.append([xt, yt, 0])

    n = len(a)

    def distance(i, j):
        x1, y1, r1 = a[i]
        x2, y2, r2 = a[j]

        dx = x1 - x2
        dy = y1 - y2

        d = math.hypot(dx, dy)
        d -= (r1 + r2)

        if d < 0:
            d = 0

        return d

    graph = []

    for _ in range(n):
        graph.append([])

    for i in range(n):
        for j in range(i + 1, n):
            d = distance(i, j)
            graph[i].append((j, d))
            graph[j].append((i, d))

    dist = []

    for _ in range(n):
        dist.append(float('inf'))

    dist[0] = 0

    pq = []

    pq.append((0, 0))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))

    return dist[-1]


xs, ys, xt, yt = map(int, input().split())

N = int(input())

a = []

for _ in range(N):
    x, y, r = map(int, input().split())
    a.append([x, y, r])

print(solve(xs, ys, xt, yt, N, a))