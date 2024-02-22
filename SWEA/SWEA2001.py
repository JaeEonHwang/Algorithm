import sys
sys.stdin = open("input.txt", "r")



T = int(input())
for i in range(1,T+1):
    most_killed = 0
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    for row in range(N-M+1):
        for col in range(N-M+1):
            fly = 0
            for delta_row in range(M):
                for delta_col in range(M):
                    fly += arr[row+delta_row][col+delta_col]
                if most_killed < fly:
                    most_killed = fly
    print(f'#{i} {most_killed}')


