import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())
road = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split(' '))
    road[s].append((e, c))
    # road[e].append((s, c))
start, end = map(int, input().split(' '))
visited = [-1]*(N+1)
visited[start] = 0
road[start].sort(key=lambda x: x[1])
arrival = start
node = road[start]
dist = 0
while True:
    if visited[node[0][0]] >= 0:
        node.pop(0)
        continue
    visited[node[0][0]] = node[0][1]
    if node[0][0] == end:
        print(visited[end])
        break
    for a, b in road[node[0][0]]:
        node.append((a, b + node[0][1]))
    node.pop(0)
    road[start].sort(key=lambda x: x[1])


