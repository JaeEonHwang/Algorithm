import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque([N])
    v = [0] * 1000001
    while q:
        k = q.popleft()
        if k == M:
            print(f'#{tc} {v[k]}')
            break
        for n in (k - 1, k + 1, k * 2, k - 10):
            if 0 <= n <= 1000000 and v[n] == 0:
                v[n] = v[k] + 1
                q.append(n)




