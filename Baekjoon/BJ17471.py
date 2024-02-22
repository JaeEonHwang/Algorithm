import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

# 선거구가 정상적으로 나뉘어 졌는지 확인 후 인구 차 구하는 함수
def election(t):
    global min_v
    a = []   # 조합에 들어있는 마을 추가
    b = []   # 조합에 들어있지 않는 마을 추가
    for i in range(N):
        if i in t:
            a.append(i)
        else:
            b.append(i)
    if bfs(maps, a) and bfs(maps, b):      # bfs 돌아서 각 선거구의 모든 마을이 연결되어있으면
        asum = 0
        bsum = 0
        for i in range(N):
            if i in a:
                asum += voters[i]   # 각 선거구 인구 더하기
            else:
                bsum += voters[i]
        if abs(asum - bsum) < min_v:  # 두 선거구 차 확인 후 업데이트
            min_v = abs(asum - bsum)

# bfs로 각 선거구의 마을이 연결되어 있는지 확인
def bfs(arr, lst):
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return True
    else:
        visited = [0] * N
        visited[lst[0]] = 1
        stack = [lst[0]]
        while stack:
            for i in range(N):
                if i in lst and visited[i] == 0 and arr[stack[0]][i] == 1:
                    visited[i] = 1
                    stack.append(i)
            stack.pop(0)
        for i in lst:
            if visited[i] == 0:
                return False
        return True


N = int(input())
voters = list(map(int, input().split()))
maps = []
town = []
areas = []
for i in range(N):
    maps.append([0] * N)   # arr 생성
    town.append(i)         # 조합 생성을 위한 마을 정보 모으기
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(1, len(a)):
        maps[i][a[j]-1] = 1   # 두 마을이 연결되어 있으면 arr에 1 표시
for i in range(N//2 + 1):
    areas.extend(list(combinations(town, i)))   # 모든 조합 구하기, N//2 + 1까지만 해도 모든 경우의 수가 확인 됨
min_v = 1001
for area in areas:    # 모든 조합 확인
    election(area)
if min_v == 1001:
    print(-1)
else:
    print(min_v)