import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T + 1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    delta_row = [1,-1,0,0]
    delta_col = [0,0,1,-1]
    max_pop = 0
    for row in range(0,N):
        for col in range(0,M):
            pop = arr[row][col]
            for i in range(4):
                if 0 <= row+delta_row[i] < N and 0 <= col+delta_col[i] < M:
                    pop += arr[row+delta_row[i]][col+delta_col[i]]
            if pop > max_pop:
                max_pop = pop
    print(f'#{tc} {max_pop}')


# 풍선 하나가 터지면, 상하좌우 풍선이 터진다
# 상하좌우 풍선이 터지지 못하면, 풍선은 터트리지 못한다

