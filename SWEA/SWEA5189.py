import sys
sys.stdin = open("input.txt", "r")


def perm(i, k):
    global min_v
    if i == k:
        total = 0
        for j in range(1, N):
            total += dstr[p[j-1]][p[j]]
        total += dstr[p[N-1]][0]
        if total < min_v:
            min_v = total
    else:
        for j in range(1, N):
            if used[j] == 0:
                p[i] = j
                used[j] = 1
                perm(i+1, k)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dstr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    used[0] = 1
    p = [-1] * N
    p[0] = 0
    min_v = 100 * N
    perm(1, N)
    print(f'#{tc} {min_v}')