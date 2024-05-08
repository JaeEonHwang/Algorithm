from itertools import combinations

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
liquid = list(map(int, input().split()))
total = 3000000001
ans = []
combs = combinations(liquid, 3)
for comb in combs:
    if abs(sum(comb)) < total:
        total = abs(sum(comb))
        ans = comb
        if ans == 0:
            break
print(" ".join(map(str, sorted(ans))))
