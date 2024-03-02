import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappop, heappush
from copy import copy


# x에서 각 지점으로 갈 때 최소 거리 구하는 함수
def dijkstra1(x):
    visited = [0] * (N + 1)
    visited[0] = 1
    visited[x] = 1
    nodes = copy(roads[x])
    while 0 in visited:
        t1, e1 = heappop(nodes)
        if visited[e1] != 1:
            visited[e1] = 1
            time[e1] = t1
            for t2, e2 in roads[e1]:
                if visited[e2] != 1:
                    heappush(nodes, (t1 + t2, e2))
        else:
            continue
    return


# 일반적인 다익스트라
def dijkstra2(s, e):
    visited = [-1] * (N + 1)
    visited[0] = 1
    visited[s] = 0
    nodes = copy(roads[s])
    while visited[e] == -1:
        t1, e1 = heappop(nodes)
        if visited[e1] == -1:
            visited[e1] = t1
            for t2, e2 in roads[e1]:
                if visited[e2] == -1:
                    heappush(nodes, (t1 + t2, e2))
    return visited[e]


N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for m in range(M):
    s, e, t = map(int, input().split())
    heappush(roads[s], (t, e))
time = [0] * (N+1)
# x에서 각 지점으로 갈 때 최소 거리를 time에 저장
dijkstra1(X)
# 각 지점에서 X까지 갈 때 최소거리를 time에 더함
for idx in range(1, N+1):
    time[idx] += dijkstra2(idx, X)
print(max(time))
