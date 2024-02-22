import sys
sys.stdin = open('input.txt', 'r')


from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    q = []
    heappush(q, (int(arr[0][0]), 0, 0)) # 누적복구시간, r, c
    while q:
        t, r, c = heappop(q)
        if r == N - 1 and c == N - 1:
            print(f'#{tc} {t}')
            break
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0 <= r + dr < N and 0 <= c + dc < N:
                try:
                    if arr[r + dr][c + dc] > int(arr[r][c]) + int(arr[r + dr][c + dc]):
                        arr[r + dr][c + dc] = int(arr[r][c]) + int(arr[r + dr][c + dc])
                        heappush(q, (arr[r + dr][c + dc], r + dr, c + dc))
                except:
                    arr[r + dr][c + dc] = int(arr[r][c]) + int(arr[r + dr][c + dc])
                    heappush(q, (arr[r + dr][c + dc], r + dr, c + dc))
