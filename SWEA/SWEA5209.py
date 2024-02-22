import sys
sys.stdin = open("input.txt", "r")


def money(k, lst):
    global total
    global min_v
    if total > min_v:
        return
    if k == N:
        if total < min_v:
            min_v = total
            return
    else:
        for i in range(N):
            if i not in lst:
                lst.append(i)
                total += cost[k][i]
                money(k + 1, lst)
                lst.pop()
                total -= cost[k][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_v = 99 * N
    total = 0
    money(0, [])
    print(f'#{tc} {min_v}')