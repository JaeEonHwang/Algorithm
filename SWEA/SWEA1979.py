import sys
sys.stdin = open("input.txt", "r")


def my_append(lst,num):
    new_list = [0] * (len(lst) + 1)
    for i in range(len(lst)):
        new_list[i] = lst[i]
    new_list[-1] = num
    return new_list


T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    fixed_arr = [[0]*(N+2) for _ in range(N+2)]
    for row in range(N):
        for col in range(N):
            fixed_arr[row+1][col+1] = arr[row][col]
    count = 0
    for row in range(N+2):
        for col in range(N+2-M-1):
            row_check_list = []
            for i in range(M+2):
                row_check_list = my_append(row_check_list,fixed_arr[row][col+i])
            if row_check_list == [0] + [1]*M + [0]:
                count += 1
    for row in range(N+2-M-1):
        for col in range(N+2):    
            col_check_list = []
            for i in range(M+2):
                col_check_list = my_append(col_check_list,fixed_arr[row+i][col])
            if col_check_list == [0] + [1]*M + [0]:
                count += 1
    print(f'#{tc} {count}')


