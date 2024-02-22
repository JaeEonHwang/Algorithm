import sys
sys.stdin = open('input.txt', 'r')

# office 2차원 리스트에서 cctv의 모든 방향을 검사하며 제일 많은 방을 감시할 경우 확인 예정
# k는 cctv 하나씩 확인할 때마다 1씩 늘어남
def monitor(arr, lst, k):
    global max_v
    global room
    if k == len(lst):  # k가 cctv 개수와 같아지면 감시할 수 있는 최대 방의 개수 업데이트
        if max_v < len(room):
            max_v = len(room)
    else:
        temp = [[], [], [], []]     # 각 방향에 대해서 감시할 수 있는 방 저장 예정
        r, c = lst[k][0], lst[k][1]  # cctv 인덱스
        point = arr[r][c]            # cctv 위치
        for i in range(4):          # 각 방향에 대해서 감시할 수 있는 방 temp[i] 인덱스에 저장
            d, rd, cd = 1, delta[i][0], delta[i][1]
            while 0 <= r + d * rd < N and 0 <= c + d * cd < M and arr[r + d * rd][c + d * cd] != 6:
                if arr[r + d * rd][c + d * cd] == 0:
                    temp[i].append((r + d * rd, c + d * cd))
                d += 1
        if point == 1:       # 1번 cctv라면
            for i in range(4):    # temp에 저장된 4개에 대해서
                new = 0           # 이번 재귀에서 새로 추가된 빈 방 개수
                for j in range(len(temp[i])):
                    if temp[i][j] not in room:   # 감시 가능 리스트에 없으면
                        room.append(temp[i][j])  # 감시 가능 리스트에 추가
                        new += 1                 # 추가된 빈 방 개수 구하기
                monitor(arr, lst, k+1)           # 다음 cctv에 대해서 재귀 돌리기
                for _ in range(new):             # 만약 탐색을 다하고 돌아왔다면 새로 추가된 방은 room 리스트에서 빼주기
                    room.pop()
        elif point == 2:      # 2번 cctv 라면
            for i in range(2):        # 상하 & 좌우만 확인하면 돼서 2번만 반복
                new = 0
                for j in range(len(temp[i])):          # 확인할 방향 1
                    if temp[i][j] not in room:
                        room.append(temp[i][j])
                        new += 1
                for j in range(len(temp[i + 2])):      # 확인할 방향 2
                    if temp[i + 2][j] not in room:
                        room.append(temp[i + 2][j])
                        new += 1
                monitor(arr, lst, k + 1)
                for _ in range(new):
                    room.pop()
        elif point == 3:         # 3번 cctv
            for i in range(4):   # 경우의 수 4가지
                new = 0
                for j in range(len(temp[i])):          # 확인할 방향 1
                    if temp[i][j] not in room:
                        room.append(temp[i][j])
                        new += 1
                for j in range(len(temp[(i + 1) % 4])):        # 확인할 방향 2
                    if temp[(i + 1) % 4][j] not in room:
                        room.append(temp[(i + 1) % 4][j])
                        new += 1
                monitor(arr, lst, k + 1)
                for _ in range(new):
                    room.pop()
        elif point == 4:          # 4번 cctv
            for i in range(4):        # 경우의 수 4가지
                new = 0
                for j in range(len(temp[i])):          # 확인할 방향 1
                    if temp[i][j] not in room:
                        room.append(temp[i][j])
                        new += 1
                for j in range(len(temp[(i + 1) % 4])):    # 확인할 방향 2
                    if temp[(i + 1) % 4][j] not in room:
                        room.append(temp[(i + 1) % 4][j])
                        new += 1
                for j in range(len(temp[(i + 2) % 4])):       # 확인할 방향 3
                    if temp[(i + 2) % 4][j] not in room:
                        room.append(temp[(i + 2) % 4][j])
                        new += 1
                monitor(arr, lst, k + 1)
                for _ in range(new):
                    room.pop()
        elif point == 5:   # cctv 5번
            new = 0
            for i in range(4):   # 4 방향 모두 확인
                for j in range(len(temp[i])):
                    if temp[i][j] not in room:
                        room.append(temp[i][j])
                        new += 1
            monitor(arr, lst, k + 1)
            for _ in range(new):
                room.pop()

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []  # cctv의 위치 저장
chk = 0    # 빈 방이 아닌 곳(0이 아닌 곳) 개수 확인용
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # cctv 방향별 확인용 델타
room = []  # cctv로 감시할 수 있는 곳 추가할 예정
max_v = 0  # cctv로 감시할 수 있는 최대 방의 개수
for row in range(N):
    for col in range(M):
        if office[row][col]:   # 0이 아닌 곳 개수 세기
            chk += 1
            if office[row][col] != 6:    # cctv라면 저장
                cctv.append((row, col))
monitor(office, cctv, 0)         # office 2차원 리스트에서 cctv의 모든 방향을 검사하며 제일 많은 방을 감시할 경우 확인 예정
print(N * M - chk - max_v)  # 사무실 넓이 - (벽 + cctv) - 최대로 감시할 수 있는 방