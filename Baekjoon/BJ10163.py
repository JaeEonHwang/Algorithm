import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
arr = [[-1] * 1001 for _ in range(1001)]
box = [0] * N
color = []
for i in range(N):
    c, r, w, h = map(int, input().split())
    for j in range(c, c + w):
        for k in range(r, r + h):
            if arr[k][j] != -1:
                box[arr[k][j]] -= 1
            arr[k][j] = i
            box[i] += 1
for i in range(N):
    print(box[i])