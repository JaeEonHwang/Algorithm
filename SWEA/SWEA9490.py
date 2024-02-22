import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T + 1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    d_i = [0, -1, 0, 1]
    d_j = [1, 0, -1, 0]
    
    max_count = 0
    for row in range(N):
        for col in range(M):
            count = arr[row][col]
            for k in range(4):
                for n in range(1,arr[row][col]+1):
                    i = row + d_i[k] * n
                    j = col + d_j[k] * n
                    if 0 <= i < N and 0 <= j < M:
                        count += arr[i][j]
            if count > max_count:
                max_count = count
    print(f'#{tc} {max_count}')