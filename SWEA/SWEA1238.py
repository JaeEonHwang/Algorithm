import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = [[0]*101 for _ in range(101)]
    contact = list(map(int, input().split()))
    for i in range(int(n/2)):
        arr[contact[2*i]][contact[2*i+1]] = 1
    visited = [-1] * 101
    visited[start] = 0
    queue = [start]
    while queue:
        a = queue.pop(0)
        for i in range(101):
            if arr[a][i] == 1 and visited[i] == -1:
                visited[i] = visited[a] + 1
                queue.append(i)

    idx = -1
    for i in range(100,-1,-1):
        if visited[i] == max(visited):
            print(f'#{tc} {i}')
            break