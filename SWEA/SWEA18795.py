import sys
sys.stdin = open('input.txt', 'r')


def quick(lst, L, r):
    if L < r:
        s = partition(lst, L, r)
        quick(lst, L, s - 1)
        quick(lst, s + 1, r)


def partition(lst, L, r):
    p = lst[L]
    i = L
    j = r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[L], lst[j] = lst[j], lst[L]
    return j



T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    quick(numbers, 0, len(numbers)-1)
    print(f'#{tc} {" ".join(map(str, numbers))}')
