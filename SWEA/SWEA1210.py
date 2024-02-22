import sys

sys.stdin = open('input.txt','r')

def my_count(lst,num):
    check = 0
    for i in lst:
        if i == num:
            check +=1
    return check

going_up = 1

for T in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    
    fixed_arr = [[0]*102 for _ in range(102)]
    for row in range(0,100):
        for col in range(0,100):
            fixed_arr[row+1][col+1] = arr[row][col]

    for i in range(102):
        if fixed_arr[100][i] == 2:
            col_idx = i
            break
    row_idx = 99
    fixed_arr[100][i] = 1
    going_up = 1
    left = 1
    while row_idx != 1:
        delta_row = [1, -1, 0, 0]
        delta_col = [0, 0, 1, -1]
        checklist = []
        for i in range(4):
            drow = delta_row[i]
            dcol = delta_col[i]
            checklist.append(fixed_arr[row_idx + drow][col_idx + dcol])
        if my_count(checklist, 1) == 2:
            if going_up == 1:
                row_idx -= 1
            else:
                if left:
                    col_idx -= 1
                else:
                    col_idx += 1
        if my_count(checklist,1) == 3:
            if going_up == 1:
                going_up = 0
                if checklist[2] == 1:
                    col_idx += 1
                    left = 0
                else:
                    col_idx -= 1
                    left = 1
            else:
                going_up = 1
                row_idx -= 1
    print(f'#{tc} {col_idx-1}')