import sys

sys. stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    error = 0
    row = 0
    col = 0
    print(f'#{tc}', end=" ")
    while error < 20:
        try:
            print(arr[row][col], end='')
            if row == 4:
                col += 1
                row = 0
            else:
                row += 1
            error = 0
        except:
            error += 1
            if row == 4:
                col += 1
                row = 0
            else:
                row += 1
    print()
