import sys
sys.stdin = open('input.txt', 'r')

# 한 번의 과정 후 새로 생긴 구름의 위치를 반환해주는 함수
def rain(lst, d, s):  # lst = 구름 위치, d = 이동방향, s = 이동 거리
    temp = []
    for r, c in lst:
        r = (r + (s * delta[d][0])) % N
        c = (c + (s * delta[d][1])) % N
        temp.append((r, c)) # 이동 후 위치 저장
        arr[r][c] += 1      # 물의 양 + 1
    for r, c in temp:       # 이동 후 물의 양 업데이트
        for i in range(4):
            dr = delta[2*i][0]  # 대각선 칸의 인덱스
            dc = delta[2*i][1]
            if 0 <= r + dr < N and 0 <= c + dc < N and arr[r+dr][c+dc] >= 1:
                arr[r][c] += 1  # 대각선 칸이 존재하고 물의 양이 1 이상이면 + 1
    cloud = []
    for r in range(N):
        for c in range(N):  # 기존 바구니 전체 탐색
            if (r, c) not in temp and arr[r][c] >= 2: # 구름이 없어진 지역이 아니고, 물의 양이 2 이상이면
                arr[r][c] -= 2    # 물의 양은 -2
                cloud.append((r, c))   # 구름 생성
    return cloud  # 구름이 생성된 위치 반환


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 방향 번호에 따른 델타 설정 1
delta = ((1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0))
area = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    di, si = map(int, input().split())
    # 방향 번호에 따른 델타 설정 2
    di %= 8
    area = rain(area, di, si) # 한 번의 과정 후 새로 생긴 구름의 위치를 반환해주는 함수
total = 0
for i in range(N):
    total += sum(arr[i])
print(total)