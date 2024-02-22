import sys
sys.stdin = open("input.txt", "r")


tc = int(input())
for i in range(1,tc+1):
    arr = [['']*10 for i in range(10)]
    N = int(input())
    coloring = [list(map(int,input().split())) for _ in range(N)]
    for trial in coloring:
        color = '0'
        for row in range(10):
            for col in range(10):
                if trial[0] <= row <= trial[2] and trial[1] <= col <= trial[3]:
                    arr[row][col] += str(trial[4])
    
    purple = 0
    for row in range(10):
        for col in range(10):
            if '1' in arr[row][col] and '2' in arr[row][col]:
                purple += 1

    print(f'#{i} {purple}')


