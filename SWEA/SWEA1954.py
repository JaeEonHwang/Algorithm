import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    num = 1

    for i in range(N):
        arr[0][i] = num
        num += 1

    row = 0
    col = N-1
    for i in range(N-1):
        if i % 2 == 0:
            for _ in range(N-1-i):
                row += 1
                arr[row][col] = num
                num += 1
            for _ in range(N-1-i):
                col -= 1
                arr[row][col] = num
                num += 1
        if i % 2 == 1:
            for _ in range(N - 1 - i):
                row -= 1
                arr[row][col] = num
                num += 1
            for _ in range(N - 1 - i):
                col += 1
                arr[row][col] = num
                num += 1
    print(f'#{tc}')
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
