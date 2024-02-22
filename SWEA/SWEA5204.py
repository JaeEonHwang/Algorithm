import sys
sys.stdin = open("input.txt", "r")


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        left = []
        right = []
        mid = len(lst) // 2
        for i in range(mid):
            left.append(lst[i])
        for i in range(mid, len(lst)):
            right.append(lst[i])
        return merge(merge_sort(left), merge_sort(right))


def merge(lstl, lstr):
    global cnt
    if lstl[-1] > lstr[-1]:
        cnt += 1
    i = 0
    j = 0
    new_lst = []
    while i < len(lstl) or j < len(lstr):
        if i < len(lstl) and j < len(lstr):
            if lstl[i] < lstr[j]:
                new_lst.append(lstl[i])
                i += 1
            else:
                new_lst.append(lstr[j])
                j += 1
        elif i == len(lstl):
            new_lst.append(lstr[j])
            j += 1
        elif j == len(lstr):
            new_lst.append(lstl[i])
            i += 1
    return new_lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    sorted_lst = merge_sort(numbers)
    print(f'#{tc} {sorted_lst[N//2]} {cnt}')