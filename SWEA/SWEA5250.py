import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    d = [[1000 + N ** 2] * N for _ in range(N)]
    q = []
    d[0][0] = 0
    heappush(q, (0, 0, 0))
    while q:
        w, r, c = heappop(q)
        if (r, c) == (N-1, N-1):
            break
        for dr, dc in delta:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if area[r + dr][c + dc] > area[r][c]:
                    height = area[r + dr][c + dc] - area[r][c]
                else:
                    height = 0
                if d[r + dr][c + dc] > height + 1 + d[r][c]:
                    d[r + dr][c + dc] = height + 1 + d[r][c]
                    heappush(q, (d[r + dr][c + dc], r + dr, c + dc))
    print(f'#{tc} {d[N-1][N-1]}')






