import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy

# 2048 게임하는 함수, k는 이동 횟수
def game2048(k):
    global max_v
    if k == 5:                              # 5번 다 움직였으면
        for row in range(N):                # 최댓값 찾아서
            if max(arrs[5][row]) > max_v:   # 기존 최댓값이랑 비교
                max_v = max(arrs[5][row])
        return

    for i in range(4):     # 동서남북 네 방향에 대해서 검사
        if arrs[k+1] != arrs[k]:       #주어진 board를 수정하는 대신 복사한 arr를 수정할 예정, visited처럼 기록을 남겨놓기 위함
            arrs[k + 1] = deepcopy(arrs[k])   # k번째면 arr[k+1]에 있는 테이블을 바꿈
            arr = arrs[k + 1]                 # 만약 바꿔야 할 arr[k+1]이 이전에 바뀌었던 arr[k]와 다르면 새로 deepcopy
        else:
            arr = arrs[k + 1]                 # 같으면 그대로 진행
        if i == 0:                            # 아마 동쪽으로 이동...?
            for row in range(N):
                for col in range(N-1, 0, -1):   # 해당 열에 0을 서쪽으로 옮기는 과정
                    if arr[row][:arr[row].count(0)] == [0] * arr[row].count(0):
                        break         # 해당 열에 0이 모두 서쪽에 몰려있으면 break
                    temp = 0
                    while arr[row][col] == 0:   # 해당 열에서 동쪽에 있는 칸부터 검사하면서 만약 0이면
                        temp += 1
                        if temp > N:
                            break               # 해당 열의 모든 값이 0이면 break
                        for j in range(col):    # 해당 열의 모든 값을 동쪽으로 한 칸씩 옮김
                            arr[row][col - j] = arr[row][col - j - 1]
                        arr[row][0] = 0         # 제일 서쪽에 있는 값은 0
                for col in range(N - 1, 0, -1):    # 숫자를 동쪽으로 옮기면서 더하는 과정 (동쪽에 있는 숫자부터 확인)
                    if arr[row][col] == arr[row][col-1] and arr[row][col] != 0:  # 만약 왼쪽에 있는 숫자와 같은데 0이 아니면
                        arr[row][col] *= 2  # 해당 숫자는 2 곱하고
                        for j in range(1, col):
                            arr[row][col - j] = arr[row][col - j - 1]  # 다른 숫자는 동쪽으로 한 칸씩 옮김
                            if arr[row][col - j - 1] == 0:
                                break         # 옮기다가 0을 만나면 그만 옮기기
                        arr[row][0] = 0
        elif i == 1:           # 서쪽으로 이동, 방향만 다르고 같은 원리
            for row in range(N):
                for col in range(N - 1):
                    if arr[row][-arr[row].count(0):] == [0] * arr[row].count(0):
                        break
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(N - 1 - col):
                            arr[row][col+j] = arr[row][col + j + 1]
                        arr[row][-1] = 0
                for col in range(N - 1):
                    if arr[row][col] == arr[row][col+1] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, N - 1 - col):
                            arr[row][col + j] = arr[row][col + j + 1]
                            if arr[row][col + j + 1] == 0:
                                break
                        arr[row][-1] = 0
        elif i == 2:     # 남쪽, row/col 반대로 되어있지만 원리는 같음. 하지만 같은 열은 하나의 리스트에 있는 것이 아니기 때문에
            for col in range(N):            # 코드는 약간 다름
                for row in range(N - 1, 0, -1):
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(row):
                            arr[row-j][col] = arr[row-j-1][col]
                        arr[0][col] = 0
                for row in range(N - 1, 0, -1):
                    if arr[row][col] == arr[row - 1][col] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, row):
                            arr[row-j][col] = arr[row-j-1][col]
                            if arr[row-j-1][col] == 0:
                                break
                        arr[0][col] = 0
        elif i == 3:    # 북쪽
            for col in range(N):
                for row in range(N-1):
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(N-1-row):
                            arr[row + j][col] = arr[row + j + 1][col]
                        arr[-1][col] = 0
                for row in range(N-1):
                    if arr[row][col] == arr[row+1][col] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, N-1-row):
                            arr[row+j][col] = arr[row+j+1][col]
                            if arr[row+j+1][col] == 0:
                                break
                        arr[-1][col] = 0
        game2048(k + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
arrs = [[]] * 6   # 변경 전 2048 테이블을 저장하기 위함. arrs[k] -> k번 움직이고 나서 테이블 모양
arrs[0] = board   # 초기 값은 주어진 테이블
game2048(0)       # 0부터 시작해서 5가 되면 멈출 예정
print(max_v)