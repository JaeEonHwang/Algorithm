import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
options = []
# 빈 공간, 나중에 벽 3개 설치할 거라 -3부터 시작
safe = -3
# 연구소 확인하면서
for r in range(N):
    for c in range(M):
        # 바이러스 있는 곳이면 따로 저장
        if arr[r][c] == 2:
            virus.append((r, c))
        # 빈 곳이면 따로 저장 + 빈 공간 개수 업데이트
        elif arr[r][c] == 0:
            safe += 1
            options.append((r, c))
max_v = 0
# 벽을 3개 설치할 수 있는 모든 경우의 수
combs = combinations(options, 3)
# 각 경우의 수에 대하여
for comb in combs:
    # 감염될 공간을 infected에 추가할 예정
    infected = virus[:]
    # 빈 공간의 개수, 감염되면 -1 할 예정
    temp = safe
    # 벽 추가로 3개 설치
    for r, c in comb:
        arr[r][c] = 1
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # pop(0)을 사용하지 않는 bfs
    # infected를 애초에 길게 만들 수도 있었지만
    # 코드가 지저분해져서 포기
    s = -1
    e = len(virus) - 1
    while s < e:
        s += 1
        r, c = infected[s]
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and (nr, nc) not in infected:
                e += 1
                infected.append((nr, nc))
                temp -= 1
    # 최대값 갱신
    if temp > max_v:
        max_v = temp
    # 추가한 벽 3개는 원래대로 돌려주기
    for r, c in comb:
        arr[r][c] = 0

print(max_v)
