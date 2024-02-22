import sys
sys.stdin = open("input.txt", "r")


from itertools import combinations

def lst_max(lst):
    tmax = 0
    for m in range(M, 0, -1):
        combs = list(combinations(range(M), m))
        for comb in combs:
            tsum1 = 0
            tsum2 = 0
            for i in comb:
                tsum1 += lst[i]
                tsum2 += (lst[i] ** 2)
            if tsum1 <= C and tsum2 > tmax:
                tmax = tsum2
    return tmax

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    hives = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    bnf = [[0] * N for _ in range(N)]
    maxs = [(0, 0, 0)] * (M * 2)
    for r in range(N):
        for c in range(N - M + 1):
            cnt = 0
            hsum = 0
            bnf[r][c] = (lst_max(hives[r][c:c+M]), r, c)
            if bnf[r][c][0] > maxs[-1][0]:
                maxs[-1] = bnf[r][c]
                maxs.sort(reverse=True)
    i = 1
    while maxs[0][1] == maxs[i][1] and maxs[i][2] + M - 1 >= maxs[0][2]:
        i += 1
    ans = maxs[0][0] + maxs[i][0]
    print(f'#{tc} {ans}')
