import sys
sys.stdin = open("input.txt", "r")


def my_max(lst):
    value = lst[0]
    for num in lst:
        if num > value:
            value = num
    return value

T = int(input())
for tc in range(1,T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    check_list=[0]
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 0:
                check_list.append(0)
            else:
                check_list[-1] += 1
        check_list.append(0)
    for col in range(M):
        for row in range(N):
            if arr[row][col] == 0:
                check_list.append(0)
            else:
                check_list[-1] += 1
        check_list.append(0)
    print(f'#{tc} {my_max(check_list)}')
