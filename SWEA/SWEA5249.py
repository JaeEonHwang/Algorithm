import sys
sys.stdin = open("input.txt", "r")



def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


from heapq import heappop, heappush

# Kruskal
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    q = []
    p = [i for i in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heappush(q, (w, n1, n2))
    total = 0
    while q:
        nw, ns, ne = heappop(q)
        if find_set(ns) != find_set(ne):
            union(ns, ne)
            total += nw
    print(f'#{tc} {total}')

# Prim
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    q = []
    v = [0] * (V+1)
    v[0] = 1
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1].append((w, n2))
        arr[n2].append((w, n1))
    total = 0
    for nw, ne in arr[0]:
        heappush(q, (nw, ne))
    while q:
        nw, ne = heappop(q)
        if v[ne] == 0:
            total += nw
            v[ne] = 1
            for w, e in arr[ne]:
                heappush(q, (w, e))
    print(f'#{tc} {total}')