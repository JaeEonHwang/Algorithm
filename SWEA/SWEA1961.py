import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        answer = ''
        for row in range(N-1,-1,-1):
            answer += str(arr[row][i])
        answer += ' '
        for col in range(N-1,-1,-1):
            answer += str(arr[N-1-i][col])
        answer += ' '
        for row in range(N):
            answer += str(arr[row][N-1-i])
        print(answer)
