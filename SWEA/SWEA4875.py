import sys
sys.stdin = open('input.txt', 'r')

def find(row,col,stack):
    while row != final_row or col != final_col:
        arr[row][col] = 1
        for i in range(4):
            rdelta, cdelta = delta[i]
            if 0 <= row + rdelta < N and 0 <= col + cdelta < N and arr[row + rdelta][col + cdelta] != 1:
                stack.append((row, col))
                row += rdelta
                col += cdelta
                if arr[row][col] == 3:
                    return True
                break
        else:
            if stack:
                row, col = stack.pop()
            else:
                return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    str_arr = [input() for _ in range(N)]
    arr = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            arr[row][col] = int(str_arr[row][col])
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row, col = (i,j)
                break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                final_row, final_col = (i,j)
                break

    stack = [(row, col)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if find(row, col, stack):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
