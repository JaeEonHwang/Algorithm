import sys
sys.stdin = open("input.txt", "r")


def minimum(m, min_sum):
    global min_v
    if m >= 12:
        if min_sum < min_v:
            min_v = min_sum
    else:
        minimum(m + 1, min_sum + plan[m] * f1)
        minimum(m + 1, min_sum + f30)
        minimum(m + 3, min_sum + f90)


T = int(input())
for tc in range(1, T + 1):
    f1, f30, f90, f365 = map(int, input().split())
    plan = list(map(int, input().split()))
    min_v = f365
    minimum(0, 0)
    print(f'#{tc} {min_v}')