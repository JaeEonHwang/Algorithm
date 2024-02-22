import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    arr[int(N/2)][int(N/2)] = arr[int(N/2+1)][int(N/2+1)] = 2
    arr[int(N/2)][int(N/2+1)] = arr[int(N/2+1)][int(N/2)] = 1
    for i in range(M):
        row, col, stone = map(int, input().split())
        arr[row][col] = stone
        delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for a, b in delta:
            new_row = row + a
            new_col = col + b
            stack = []
            while 0 < new_row <= N and 0 < new_col <= N and arr[new_row][new_col] != stone and arr[new_row][new_col]:
                stack.append((new_row, new_col))
                new_row += a
                new_col += b
            if 0 < new_row <= N and 0 < new_col <= N and arr[new_row][new_col] == stone:
                for c, d in stack:
                    if stone == 2:
                        arr[c][d] = 2
                    else:
                        arr[c][d] = 1
    count1 = 0
    count2 = 0
    for row in range(N+1):
        for col in range(N+1):
            if arr[row][col] == 1:
                count1 += 1
            elif arr[row][col] == 2:
                count2 += 1
    print(f'#{tc} {count1} {count2}')