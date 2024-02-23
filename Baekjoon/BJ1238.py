import sys
sys.stdin = open('input.txt', 'r')


def isvalid(n1, n2):
    # n1: 기존 경로, n2: 새경로
    if str(n2 % 100).count("1") > str(n1 % 100).count("1"):
        return True
    elif str(n2 % 100).count("1") < str(n1 % 100).count("1"):
        if n1 < 0:
            return True
        else:
            return False
    elif str(n2 % 100).count("1") == str(n1 % 100).count("1"):
        return True

N, E = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(E):
    node1, node2, dist = map(int, input().split())
    roads[node1].append((node2, dist*100))
    roads[node2].append((node1, dist*100))
stop1, stop2 = map(int, input().split())

# 1의자리 스팟1, 10의자리 스팟2
visited = [-100 for _ in range(N+1)]
nodes = []
for road in roads[1]:
    node, dist = road
    nodes.append((node, dist))
nodes.sort(key=lambda x: x[1])
# print(roads)
# print(visited)
# print(nodes)
while nodes:
    check = isvalid(visited[nodes[0][0]], nodes[0][1])
    if check:
        visited[nodes[0][0]] = nodes[0][1]
        if nodes[0][0] == stop1:
            visited[nodes[0][0]] += 1
        elif nodes[0][0] == stop2:
            visited[nodes[0][0]] += 10
        if nodes[0][0] == N and visited[nodes[0][0]]%100 == 11:
            print(visited[nodes[0][0]]//100)
            break
        for s, d in roads[nodes[0][0]]:
            nodes.append((s, d + visited[nodes[0][0]]))
        nodes.pop(0)
        nodes.sort(key=lambda x: x[1]//100)
    else:
        nodes.pop(0)
        continue
else:
    print(-1)