import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy


# 배열 돌리기 함수(배열, 돌린 횟수)
def rotate(arr, k):
    global min_v
    # 원하는만큼 돌렸으면 최솟값 찾기
    if k == K:
        for i in range(N):
            if sum(arr[i]) < min_v:
                min_v = sum(arr[i])
    # 배열 돌리기
    else:
        # 회전 연산 중에
        for i in range(K):
            # 아직 사용 안 한 회전 연산이 있으면
            if visited[i] == 0:
                # 사용했다고 표시하고 연산하기
                visited[i] = 1
                # 회전 연산 정보
                r, c, s = move[i]
                r -= 1
                c -= 1
                # 회전하는 정사각형 개수
                for j in range(1, s + 1):
                    # 시작점: 제일 위, 왼쪽으로 설정
                    sr, sc = r - j, c - j
                    # 시작점의 값 임시 저장
                    temp = arr[sr][sc]
                    # 델타 설정
                    d = 0
                    dr, dc = delta[d]
                    # 회전하는 정사각형의 한 변의 길이
                    limit = (j + 1) * 2 - 1
                    # 한 변에서의 이동량 체크용
                    l = 1
                    # tr, tc = 업데이트할 인덱스
                    tr = sr
                    tc = sc
                    # 업데이트에 사용해야 할 값이 시작값이 아니면
                    while not (tr + dr == sr and tc + dc == sc):
                        # 한 변에서 최대로 이동했으면 델타 업데이트, 이동량 초기화
                        if l == limit:
                            d = (d + 1) % 4
                            dr, dc = delta[d]
                            l = 1
                        # 델타만큼 움직인 칸의 값으로 업데이트
                        arr[tr][tc] = arr[tr + dr][tc + dc]
                        # 기준점 업데이트
                        tr += dr
                        tc += dc
                        # 이동량 업데이트
                        l += 1
                    # 시작점 값 업데이트
                    arr[tr][tc] = temp
                # 이동 후 배열 상태 저장
                arr_save[k+1] = deepcopy(arr)
                # 재귀(dfs)
                rotate(arr, k + 1)
                # 재귀 돌고 온 후 원상태로 복원
                visited[i] = 0
                arr = deepcopy(arr_save[k])


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(K)]
# 순열이랑 dfs 중에 dfs가 좀 더 빠를 거 같아서 dfs로 함
visited = [0] * K
# 시계 방향으로 돌 수 있게 델타 설정
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
# 돌리기 전 배열 상태 저장용 리스트, n번 인덱스에는 n번 돌아간 배열이 저장될 예정
arr_save =[0] * (K+1)
# 배열 원본 저장, 배열을 직접 조작할 거라 deepcopy 사용해서 저장
arr_save[0] = deepcopy(arr)
min_v = 100 * M
# 배열 돌리기 함수
rotate(arr, 0)
print(min_v)