from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
dct = defaultdict(list)
nums = list(map(int, input().split()))
for i in range(N-1):
    for j in range(i+1, N):
        dct[nums[i] + nums[j]].append((i, j))
ans = 0
for i in range(N):
    for opt in dct[nums[i]]:
        if i not in opt:
            ans += 1
            break
print(ans)
