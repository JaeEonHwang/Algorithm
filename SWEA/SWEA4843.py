import sys
sys.stdin = open("input.txt", "r")


def my_sort(lst):
    for e in range(len(lst)):
        max_idx = e
        for j in range(e, len(lst)):
            if lst[max_idx] < lst[j]:
                max_idx = j
        lst[e], lst[max_idx] = lst[max_idx], lst[e]
    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    my_sort(numbers)
    print(f'#{tc}', end=' ')
    for i in range(10):
        if i % 2 == 0:
            print(numbers[i//2], end=' ')
        else:
            print(numbers[N - 1 - i // 2], end=' ')
    print()
