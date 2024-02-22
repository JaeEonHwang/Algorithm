import sys
sys.stdin = open("input.txt", "r")


def row_check(arr): 
    for row in range(9):
        if len(set(arr[row])) != 9:
            return 0
    else:
        return 1


def col_check(arr): 
    for col in range(9):
        new_list = []
        for row in range(9):
            new_list.append(arr[row][col])
        if len(set(new_list)) != 9:
            return 0
    else:
        return 1
    
def box_check(arr):
    rdelta = [1, 0, -1]
    cdelta = [1, 0, -1]
    for row in range(1,9,3):
        for col in range(1,9,3):
            new_list = []
            for r in rdelta:
                for c in cdelta:
                    new_list.append(arr[row+r][col+c])
            if len(set(new_list)) != 9:
                return 0
    else:
        return 1


T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    a = row_check(arr)
    b = col_check(arr)
    c = box_check(arr)
    print(f'#{tc} {a*b*c}')


