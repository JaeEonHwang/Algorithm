import sys
sys.stdin = open("input.txt", "r")


def bus(k):
    global min_v
    global cnt
    if cnt >= min_v:
        return
    if k >= N:
        if cnt < min_v:
            min_v = cnt
            return
    else:
        for i in range(info[k], 0, -1):
            cnt += 1
            bus(i + k)
            cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    info = list(map(int, input().split()))
    N = info[0]
    min_v = 100
    cnt = -1
    bus(1)
    print(f'#{tc} {min_v}')