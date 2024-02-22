import sys
sys.stdin = open("input.txt", "r")


def my_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total


for test in range(10):
    tc  = int(input())
    arr = [list(map(int,input().split())) for i in range(100)]

    row_max = 0
    for i in arr:
        if my_sum(i) > row_max:
            row_max = my_sum(i)
    
    col_max = 0
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_sum > col_max:
            col_max = col_sum

    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += arr[i][i]
    diagonal_max = diagonal_sum

    diagonal_sum = 0       
    for i in range(100):
        diagonal_sum += arr[i][99-i]
    if diagonal_sum > diagonal_max:
        diagonal_max = diagonal_sum

    MAX = row_max
    if col_max > MAX:
        MAX = col_max
    if diagonal_max > MAX:
        MAX = diagonal_max
    
    print(f'#{tc} {MAX}')