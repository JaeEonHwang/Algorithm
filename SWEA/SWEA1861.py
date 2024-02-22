import sys
sys.stdin = open('input.txt', 'r')


def moving(arr, rw, cl, n):
    global move
    global max_v
    global point
    for r, c in delta:
        if 0 <= rw + r < n and 0 <= cl + c < n and rooms[rw][cl] - 1 == rooms[rw+r][cl+c]:
            move += 1
            moving(arr, rw+r, cl+c, n)
            break
    else:
        if move > max_v:
            max_v = move
            point = arr[rw][cl]
        elif move == max_v:
            if point > arr[rw][cl]:
                point = arr[rw][cl]
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    point = N ** 2
    max_v = 0
    for row in range(N):
        for col in range(N):
            move = 0

            moving(rooms, row, col, N)
    print(f'#{tc} {point} {max_v + 1}')