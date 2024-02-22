import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    
    start = 0
    for row in range(N):
        for col in range(N-M+1):
            check_list1 = []
            for i in range(M):
                check_list1.append(arr[row][col+i])
            check_lsit2 = check_list1[::-1]
            if check_list1 == check_lsit2:
                print(f'#{tc} {"".join(check_list1)}')
    
    start = 0
    for col in range(N):
        for row in range(N-M+1):
            check_list1 = []
            for i in range(M):
                check_list1.append(arr[row+i][col])
            check_lsit2 = check_list1[::-1]
            if check_list1 == check_lsit2:
                print(f'#{tc} {"".join(check_list1)}')