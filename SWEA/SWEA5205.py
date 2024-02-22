import sys
sys.stdin = open("input.txt", "r")


def quick(lst, s, e):
    if s < e:
        a = partition(lst, s, e)
        quick(lst, s, a - 1)
        quick(lst, a + 1, e)


def partition(lst, s, e):
    p = lst[s]
    i = s
    j = e
    while i <= j:
        while i <= j and p >= lst[i]:
            i += 1
        while i <= j and p <= lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[s], lst[j] = lst[j], lst[s]
    return j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    quick(numbers, 0, N-1)
    print(f'#{tc} {numbers[N//2]}')