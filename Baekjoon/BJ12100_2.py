import sys
sys.stdin = open('input.txt', 'r')

import copy


def game2048(ARR, n, d, move):
    global max_v
    global cnt
    arr = copy.deepcopy(ARR)
    arrs[move] = arr
    if move == 6:
        cnt += 1
        #print(arr)
        for row in range(n):
            for col in range(n):
                if arr[row][col] > max_v:
                    max_v = arr[row][col]
    else:
        for i in range(drt[d][0][0], drt[d][0][1], drt[d][0][2]):
            for j in range(drt[d][0][0], drt[d][0][1], drt[d][0][2]):
                if arr[i][j] == 0:
                    while arr[i][j] == 0:
                        for k in range(0, n):
                            if 0 <= i+(k+1)*drt[d][2] < n and 0 <= j+(k+1)*drt[d][3] < n:
                                arr[i+k*drt[d][2]][j+k*drt[d][3]] = arr[i+(k+1)*drt[d][2]][j+(k+1)*drt[d][3]]
                            else:
                                arr[i+k*drt[d][2]][j+k*drt[d][3]] = 0
                                break
                        else:
                            break
            for j in range(drt[d][0][0], drt[d][0][1], drt[d][0][2]):
                if 0 <= i + drt[d][2] < n and 0 <= j + drt[d][3] < n and arr[i][j] == arr[i + drt[d][2]][j + drt[d][3]]:
                    arr[i][j] *= 2
                    for k in range(1, n):
                        if 0 <= i+(k+1)*drt[d][2] < n and 0 <= j+(k+1)*drt[d][3] < n:
                            arr[i + k * drt[d][2]][j + k * drt[d][3]] = arr[i + (k + 1) * drt[d][2]][j + (k + 1) * drt[d][3]]
                        else:
                            arr[i + k * drt[d][2]][j + k * drt[d][3]] = 0
                            break
                else:
                    continue
        for a in range(4):
            game2048(arrs[move], n, a, move + 1)
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
# 0, 1, 2, 3 = 동, 서, 남, 북
drt = {0: ((N-1, -1, -1), (N-1, -1, -1), 0, -1),
       1: ((0, N, 1), (N-1, -1, -1), 0, 1),
       2: ((N-1, -1, -1), (N-1, -1, -1), -1, 0),
       3: ((0, N, 1), (0, N, 1), 1, 0)}
max_v = 0
arrs = [0] * 7
arrs[0] = table
cnt = 0
for b in range(4):
    game2048(arrs[0], N, b, 1)
print(max_v)