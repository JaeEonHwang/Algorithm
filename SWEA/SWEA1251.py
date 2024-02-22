import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    arr = [999e999] * N
    arr[0] = 0
    v = [0] * N
    q = []
    total = 0
    heappush(q, (0, 0))  # 비용, 섬번호
    while q:
        cost, island = heappop(q)
        v[island] = 1
        for i in range(N):
            if i == island or v[i] == 1:
                continue
            new_cost = (xs[i] - xs[island]) ** 2 + (ys[i] - ys[island]) ** 2
            if arr[i] > new_cost:
                arr[i] = new_cost
                heappush(q, (new_cost, i))
    print(f'#{tc} {round(sum(arr) * E)}')
