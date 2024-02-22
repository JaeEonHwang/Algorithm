import sys
sys.stdin = open('input.txt', 'r')


def babygin(lst):
    if lst[0] == lst[1] == lst[2]:
        return True
    elif lst[0] == lst[1] - 1 == lst[2] - 2:
        return True
    else:
        return False


def perm(i, k):
    global result
    if i == k:
        if babygin(p[:3]) and babygin(p[3:]):
            result = 1
            return
    else:
        for j in range(6):
            if used[j] == 0:
                used[j] = 1
                p[i] = int(number[j])
                perm(i + 1, k)
                used[j] = 0


T = int(input().strip())
for tc in range(1, T+1):
    number = input().strip()
    p = [-1] * 6
    used = [0] * 6
    result = 0
    perm(0, 6)
    print(f'#{tc} {result}')
