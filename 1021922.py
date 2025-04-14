#!/usr/bin/python

import sets
import sys

def find(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, x, y):
    find(parent, x)
    find(parent, y)

    if parent[x] != parent[y]:
        parent[parent[y]] = parent[parent[x]]

def main(argv):
    tokens = sys.stdin.readline().rstrip("\n").split()

    while len(tokens) == 3:
        n, k, l = [int(i) for i in tokens]

        parent_roads = [int(i) for i in xrange(n)]
        parent_railways = [int(i) for i in xrange(n)]

        for i in xrange(k):
            x, y = [int(i) for i in raw_input().split(" ")]
            union(parent_roads, x - 1, y - 1)

        for i in xrange(l):
            x, y = [int(i) for i in raw_input().split(" ")]
            union(parent_railways, x - 1, y - 1)

        count = dict()
        for i in xrange(n):
            key = (find(parent_roads, i), find(parent_railways, i))
            if not count.has_key(key):
                count[key] = 0
            count[key] += 1

        results = []
        for i in xrange(n):
            key = (find(parent_roads, i), find(parent_railways, i))
            results.append(str(count[key]))
        print " ".join(results)

        tokens = sys.stdin.readline().rstrip("\n").split()

if __name__ == "__main__":
    main(sys.argv)