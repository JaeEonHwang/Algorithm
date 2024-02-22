import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
arr = [[0] * (V+1) for _ in range(V+1)]
routes = list(map(int, input().split()))
for i in range(E):
    x = i * 2
    y = i * 2 + 1
    arr[routes[x]][routes[y]] = 1
    arr[routes[y]][routes[x]] = 1
visited = [0] * (V+1)
visited[1] = 1
stack = [1]
result = [1]
a = 1
while stack:
    for idx in range(V+1):
        if arr[a][idx] == 1 and visited[idx] == 0:
            stack.append(idx)
            visited[idx] = 1
            result.append(idx)
            a = idx
            break
    else:
        stack.pop()
        try:
            a = stack[-1]
        except:
            print(f'#1 {"-".join(map(str,result))}')
