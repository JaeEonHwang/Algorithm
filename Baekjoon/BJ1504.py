import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(s, e):
    nodes = roads[s]
    visited = [-1] * (N+1)
    visited[s] = 0
    nodes.sort(key=lambda x:x[1])
    while nodes:
        if visited[nodes[0][0]] != -1:
            nodes.pop(0)
            continue
        visited[nodes[0][0]] = nodes[0][1]
        for spot, dist in roads[nodes[[0][0]]:
            nodes.append((spot, dist + nodes[0][1]))
    return visited

N, E = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(E):
    node1, node2, dist = map(int, input().split())
    roads[node1].append((node2, dist))
    roads[node2].append((node1, dist))
stop1, stop2 = map(int, input().split())
print(roads)
print(dijkstra(1,1))