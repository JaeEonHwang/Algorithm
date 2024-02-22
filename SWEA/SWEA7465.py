import sys
sys.stdin = open("input.txt", "r")


from heapq import heappop, heappush

def bfs(n):
    global cnt
    lst = []
    heappush(lst, n)
    while lst:
        a = heappop(lst)
        for i in close[a]:
            if v[i] == 0:
                v[i] = 1
                heappush(lst, i)
    cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    close = [[] for _ in range(N + 1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        close[p1].append(p2)
        close[p2].append(p1)
    v = [0] * (N + 1)
    v[0] = 1
    cnt = 0
    while 0 in v:
        for i in range(1, N + 1):
            if v[i] == 0:
                v[i] = 1
                bfs(i)
    print(f'#{tc} {cnt}')