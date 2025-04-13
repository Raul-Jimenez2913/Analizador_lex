#!/usr/bin/env python
# -*- coding: utf-8 -*-

MINUS_INF = -1000000000

n, m, y, z = map(int, raw_input().split())

decode = {}
p = range(m) 
for i in xrange(m):
    ipt = raw_input().split()
    decode[ipt[0]] = i
    p[i] = int(ipt[1])

b = raw_input()

# dp[i][j][k]: i個目のブロックまでで、一番上の色jでありかつ集合kの色を使用済みであるとき　の最高得点
dp = [[[MINUS_INF for k in xrange(1 << m)] for j in xrange(m)] for i in xrange(n)]
fpiece = decode[b[0]]
dp[0][fpiece][1 << fpiece] = p[fpiece]
for i in xrange(0, n):
    for j in xrange(m):
        dp[i][j][0] = 0

for i in xrange(1, n):
    for j in xrange(m):
        for k in xrange(1 << m):
            if (k & (1 << j)) != 0:
                # 今落ちてきた色がj色だった場合
                if decode[b[i]] == j:
                    for h in xrange(m):
                        if dp[i - 1][h][k] != MINUS_INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][h][k] + p[j] + (y if h == j else 0))
                        k_tmp = k & (~(1 << j))
                        if dp[i - 1][h][k_tmp] != MINUS_INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][h][k_tmp] + p[j])
                # j色じゃなかった場合
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
                
ans = 0
for j in xrange(m):
    for k in xrange(1 << m):
        if dp[n - 1][j][k] != MINUS_INF:
            ans = max(ans, dp[n - 1][j][k] + (z if k == ((1 << m) - 1) else 0))
            
print ans
