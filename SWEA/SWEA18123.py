import sys
sys.stdin = open("input.txt", "r")


def abs_minus(num1, num2):
    if num1 > num2:
        return (num1 - num2)
    else:
        return (num2 - num1)

delta_row = [1, 0, -1, 0]
delta_col = [0, 1, 0, -1]



cases = int(input())
for tc in range(1,cases + 1):
    total = 0
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    for row in range(N):
        for col in range(N):
            center = arr[row][col]
            for delta in range(4):
                if 0 <= row + delta_row[delta] < N and 0 <= col + delta_col[delta] < N:
                    total += abs_minus(center,arr[row + delta_row[delta]][col + delta_col[delta]])
    print(f'#{tc} {total}')