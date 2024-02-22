import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)


def side_max(bottom, floor, n):
    global total
    side = []
    top = bottom_top[dices[floor].index(bottom)]
    for i in range(6):
        if bottom != dices[floor][i] and i != top:
            side.append(dices[floor][i])
    total += max(side)
    if total + (n - floor) * 6 < max_v:
        return 0
    if floor == n:
        return total
    else:
        return side_max(dices[floor][top], floor + 1, n)


bottom_top = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
for i in range(6):
    total = 0
    a = side_max(dices[0][i], 0, N - 1)
    if a > max_v:
        max_v = a
print(max_v)
