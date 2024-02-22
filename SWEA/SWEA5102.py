import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    S, G = map(int, input().split())
    queue = [0] * V
    visited = [-1] * (V+1)
    queue[0] = S
    visited[S] = 0
    front = -1
    rear = 0

    result = False
    while front != rear:
        front += 1
        a = queue[front]
        for i in range(1, V+1):
            if arr[a][i] == 1 and i == G:
                result = True
                front = rear
                break
            elif arr[a][i] == 1 and visited[i] == -1:
                rear += 1
                queue[rear] = i
                visited[i] = visited[a] + 1
    if result:
        print(f'#{tc} {visited[a]+1}')
    else:
        print(f'#{tc} 0')
