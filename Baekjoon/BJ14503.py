import sys
sys.stdin = open('input.txt', 'r')


# 규칙에 따라 청소하는 함수
def clean(r, c, d):  # r, c: 도착한 칸의 인덱스, d: 방향
    global cnt
    if room[r][c] == 0:   # 도착한 곳이 청소 안 한 곳이면
        cnt += 1          # 청소 횟수 +1 하고
        room[r][c] = 2    # 청소했다는 표시하기
    if surround(r, c):    # 주면에 청소 안 한 칸이 있으면
        d = (d+3)%4       # delta에 방향이 북-동-남-서로 설정되어있어서  반시계로 돌려면 +3씩 해줘야함
        for _ in range(4):
            if 0 <= r+delta[d][0] < N and 0 <= c+delta[d][1] < M:  # 델타이동한 인덱스가 유효하면
                if room[r+delta[d][0]][c+delta[d][1]]:   # 그리고, 벽(1)이거나 청소를 한 구역(2)이면
                    d = (d+3)%4                          # 반시계로 돌기
                else:
                    break       # 유효한 인덱스인데 청소를 안 한 구역이면 반시계 방향으로 도는 거 멈추기
            else:
                d = (d + 3) % 4   # 유효한 인덱스가 아니면 반시계 방향으로 돌기
        clean(r + delta[d][0], c + delta[d][1], d)  # 청소 안 한 방향으로 이동해서 clean 함수 재귀
    # 주변에 청소 안 한 칸이 없으면
    else:
        # 뒤로 이동했을 때 유효한 인덱스가 아니거나, 벽(1)이면 return (청소 그만)
        if r-delta[d][0] < 0 or r-delta[d][0] >= N or c-delta[d][1] < 0 or c-delta[d][1] >= M or room[r-delta[d][0]][c-delta[d][1]] == 1:
            return
        else:
            # 유효한 인덱스 + 벽이 아니면 뒤로 한 칸 가서 clean 재귀
            clean(r-delta[d][0], c-delta[d][1], d)


# 주변에 청소 안 한 칸이 있는지 찾는 함수
def surround(r, c):
    for dr, dc in delta:
        if 0 <= r + dr < N and 0 <= c + dc < M and room[r+dr][c+dc] == 0:
            return True
    return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서 (반시계 방향이 아님!!ㅠ)
cnt = 0
clean(r, c, d)
print(cnt)