import sys
sys.stdin = open("input.txt", "r")


def my_extend(lst1, lst2):
    new_list = [0] * (len(lst1) + len(lst2))
    for i in range(len(lst1)):
        new_list[i] = lst1[i]
    for i in range(len(lst2)):
        new_list[i+len(lst1)] = lst2[i]
    return new_list


def my_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    whole_list = []
    for i in range(N):
        numbers = list(map(int, input().split()))
        whole_list = my_extend(whole_list, numbers)
    my_sort(whole_list)
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        arr[0][i] = whole_list[i]

    row = 0
    col = N-1
    num = N
    for i in range(N-1):
        if i % 2 == 0:
            for _ in range(N-1-i):
                row += 1
                arr[row][col] = whole_list[num]
                num += 1
            for _ in range(N-1-i):
                col -= 1
                arr[row][col] = whole_list[num]
                num += 1
        if i % 2 == 1:
            for _ in range(N - 1 - i):
                row -= 1
                arr[row][col] = whole_list[num]
                num += 1
            for _ in range(N - 1 - i):
                col += 1
                arr[row][col] = whole_list[num]
                num += 1
    print(f'#{tc}')
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
