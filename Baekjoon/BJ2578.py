import sys
sys.stdin = open('input.txt', 'r')

def count_bingo(arr):
    total = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            total += 1
    for i in range(5):
        if arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i] == 0:
            total += 1
    if arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0] == 0:
        total += 1
    if arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] == 0:
        total += 1
    return total

def find_number(arr,n):
    for row in range(5):
        for col in range(5):
            if arr[row][col] == call[n]:
                arr[row][col] = 0
                return


bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
for i in range(5):
    call.extend(list(map(int, input().split())))
for i in range(12):
    find_number(bingo, i)

trial = 12
while count_bingo(bingo) < 3:
    find_number(bingo, trial)
    trial += 1

print(trial)


