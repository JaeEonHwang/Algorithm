import sys
sys.stdin = open("input.txt", "r")


def perm(a, k, n, s):
    global min_v
    if sum(p[:a]) >= min_v:
        return
    if a == k:
        if sum(p) < min_v:
            min_v = sum(p)
    else:
        for j in range(n ** 2):
            if used[j] == 0 and arr[s][j] == 1:
                used[j] = 1
                p[a] = table[j]
                perm(a + 1, k, n, j)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    table = []
    for _ in range(N):
        table.extend(list(map(int, input().split())))
    arr = [[0] * N ** 2 for _ in range(N ** 2)]
    for i in range(N ** 2):
        if i // N == N - 1:
            if i % N != N - 1:
                arr[i][i + 1] = 1
        else:
            arr[i][i + N] = 1
            if i % N != N - 1:
                arr[i][i + 1] = 1
    p = [0] * (2 * N - 1)
    p[0] = table[0]
    used = [0] * N ** 2
    min_v = 10 * N
    perm(1, 2 * N - 1, N, 0)
    print(f'#{tc} {min_v}')

