import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    queue = [0] * N * M
    front = -1
    rear = 0
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 'W':
                queue[rear] = (row, col)
                dist[row][col] = 0
                rear += 1
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    total = 0
    while front < rear - 1:
        front += 1
        row, col = queue[front]
        for rd, cd in delta:
            if 0 <= row + rd < N and 0 <= col + cd < M and dist[row+rd][col+cd] == -1:
                dist[row + rd][col + cd] = dist[row][col] + 1
                total += dist[row + rd][col + cd]
                queue[rear] = (row + rd, col + cd)
                rear += 1
    print(f'#{tc} {total}')

