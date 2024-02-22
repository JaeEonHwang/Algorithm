import sys
sys.stdin = open('input.txt', 'r')


from math import floor


# (행 델타, 열 델타, 비율) 넣어주면 모래를 옮겨줌
# 유효 인덱스가 아니면 값 더하기
# 옮겨진 모래량 return
def wind(dr, dc, ratio):
    global total
    if 0 <= r + dr < N and 0 <= c + dc < N:
        arr[r + dr][c + dc] += floor(center * ratio)
    else:
        total += floor(center * ratio)
    return floor(center * ratio)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
total = 0
r = N // 2   # 시작점
c = N // 2
d = 0      # 최소 이동 방향
# 재귀쓰니까 메모리 초과 떠서 for 문으로 돌림
for _ in range(N ** 2 - 1):
    temp = 0  # 다른 칸으로 옮겨지는 모래 저장용
    dr = delta[d][0]
    dc = delta[d][1]
    r += dr  # 모래가 비워질 칸의 인덱스, 다음 for문 돌 때는 시작점이 됨
    c += dc
    center = arr[r][c]    # 토네이도 때문에 모래가 없어질 칸
    # 각 칸으로 비율만큼 모래 옮기기
    # wind의 return 값 = 옮겨진 모래량
    temp += wind(2 * dr, 2 * dc, 0.05)
    temp += wind(2 * dc, 2 * dr, 0.02)
    temp += wind(- 2 * dc, - 2 * dr, 0.02)
    temp += wind(dc, dr, 0.07)
    temp += wind(-dc, -dr, 0.07)
    if dr == 0:
        temp += wind(dc, dc, 0.1)
        temp += wind(-dc, dc, 0.1)
        temp += wind(dc, -dc, 0.01)
        temp += wind(-dc, -dc, 0.01)
    else:
        temp += wind(dr, dr, 0.1)
        temp += wind(dr, -dr, 0.1)
        temp += wind(-dr, dr, 0.01)
        temp += wind(-dr, -dr, 0.01)
    # a 칸에는 다른 칸에 이동하고 남은 모래 다 옮기기
    center -= temp
    wind(dr, dc, 1)
    arr[r][c] = 0
    # 방향이 바뀌는 규칙
    if (r - c == 1 and r <= N // 2) or r + c == N - 1 or (r - c == 0 and r > N // 2):
        d = (d + 1) % 4
print(total)