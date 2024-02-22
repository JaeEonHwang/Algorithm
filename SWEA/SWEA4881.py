import sys
sys.stdin = open('input.txt', 'r')


def backtracking(k, N, s):
    global total
    if k == N:
        if total > s:
            total = s
            return
    else:
        for i in range(N):
            if i not in selected:
                if s + arr[k][i] >= total:
                    continue
                selected.append(i)
                backtracking(k+1, N, s + arr[k][i])
                selected.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = N * 10
    k = 0
    s = 0
    selected = []
    backtracking(k, N, s)

    print(f'#{tc} {total}')
