import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    idx = 1
    while info[idx] != -1:
        tree[node].append((info[idx], info[idx+1]))
        idx += 2
dist = [-1] * (V+1)
dist[0] = dist[1] = 0
stack = [1]
while -1 in dist:
    parent = stack.pop()
    for node, value in tree[parent]:
        if dist[node] == -1:
            dist[node] = dist[parent] + value
            stack.append(node)
end = dist.index(max(dist))
dist = [-1] * (V+1)
dist[0] = dist[end] = 0
stack = [end]
while -1 in dist:
    parent = stack.pop()
    for node, value in tree[parent]:
        if dist[node] == -1:
            dist[node] = dist[parent] + value
            stack.append(node)
print(max(dist))
