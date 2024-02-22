import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    queue = [0] * N * N
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                visited[row][col] = 0
                queue[0] = (row,col)

    rdelta = [1, -1, 0, 0]
    cdelta = [0, 0, 1, -1]
    front = -1
    rear = 0
    result = False
    while front != rear:
        front += 1
        a = queue[front]
        for i in range(4):
            new_row = a[0] + rdelta[i]
            new_col = a[1] + cdelta[i]
            if 0 <= new_row <N and 0 <= new_col <N and maze[new_row][new_col] == '0' and visited[new_row][new_col] < 0:
                visited[new_row][new_col] = visited[a[0]][a[1]] + 1
                rear += 1
                queue[rear] = (new_row, new_col)
            elif 0 <= new_row <N and 0 <= new_col <N and maze[new_row][new_col] == '3':
                result = True
                front = rear
                break
    if result:
        print(f'#{tc} {visited[a[0]][a[1]]}')
    else:
        print(f'#{tc} 0')
