import sys
sys.stdin = open('input.txt', 'r')

from copy import copy


# 두 지점을 이동할 때 최단 경로를 구하는 다익스트라 함수
# 시작점과 도착점이 같으면 0 반환, 갈 수 없으면 -1 반환
def dijkstra(s, e):
    if s == e:
        return 0
    nodes = copy(roads[s])
    visited = [-1] * (N+1)
    visited[s] = 0
    while nodes:
        node = min(nodes, key=lambda x: x[1])
        if visited[node[0]] != -1:
            nodes.remove(node)
            continue
        if node[0] == e:
            return node[1]
        visited[node[0]] = node[1]
        for spot, dist in roads[node[0]]:
            nodes.append((spot, dist + node[1]))
        nodes.remove(node)
    return -1


N, E = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(E):
    node1, node2, dist = map(int, input().split())
    roads[node1].append((node2, dist))
    roads[node2].append((node1, dist))
stop1, stop2 = map(int, input().split())

# 1에서 출발해서 N을 갈 때 특정 지점(2, 3)을 지나는 경우의 수: 123N/132N
road12 = dijkstra(1, stop1)
road13 = dijkstra(1, stop2)
road23 = dijkstra(stop1, stop2)
road2N = dijkstra(stop1, N)
road3N = dijkstra(stop2, N)

# 123N/132N 경우의 수 구하기
if road12 > 0 and road23 > 0 and road3N > 0:
    option1 = road12 + road23 + road3N
else:
    option1 = -1
if road13 > 0 and road23 > 0 and road2N > 0:
    option2 = road13 + road23 + road2N
else:
    option2 = -1

# 1=2이거나 3=N인 특수 경우 처리
if stop1 == 1 and stop2 == N:
    option1 = option2 = road23
elif stop1 == 1:
    option1 = option2 = road23 + road3N
elif stop2 == N:
    option1 = option2 = road12 + road23

# 불가능한 경우가 포함된 경우 처리
if min(option1, option2) > 0:
    print(min(option1, option2))
else:
    print(max(option1, option2))