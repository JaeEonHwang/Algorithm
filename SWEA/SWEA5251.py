import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(E)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s].append((e, w))
    d = [100 * E + 1] * (N + 1)
    d[0] = 0
    q = []
    heappush(q, (0, 0))
    while q:
        s, w = heappop(q)
        for ne, nw in arr[s]:
            if d[ne] > w + nw:
                d[ne] = w + nw
                heappush(q, (ne, w + nw))
    print(f'#{tc} {d[N]}')




