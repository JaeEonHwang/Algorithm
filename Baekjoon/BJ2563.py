import sys
sys.stdin = open('input.txt', 'r')

arr = [[0] * 100 for _ in range(100)]
N = int(input())
ans = 0
for _ in range(N):
    r, c = map(int, input().split())
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1
print(ans)