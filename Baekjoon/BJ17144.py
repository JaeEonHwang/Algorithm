import sys
sys.stdin = open('input.txt', 'r')

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
vacuum = []
total = 0
# 방 정보를 [a, b] 형태로 업데이트
# b에는 다른 칸에서 넘어온 먼지 추가할 예정
for r in range(R):
    for c in range(C):
        # total = 방 안에 있는 모든 먼지양
        total += room[r][c]
        room[r][c] = [room[r][c], 0]
        # -1 일이면 공기청정기로 따로 저장
        # 청소기로 착각해서 변수명 이상하게 정함;;
        if room[r][c][0] == -1:
            vacuum.append((r, c))
total += 2
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
# T초동안 반복
for _ in range(T):
    # 먼지가 흩어지는 과정
    for r in range(R):
        for c in range(C):
            # 공기청정기 있는 칸이면 패스
            if room[r][c][0] == -1:
                continue
            # cnt = 먼지가 다른 칸으로 간 횟수 저장
            cnt = 0
            # 다른 칸으로 이동할 먼지양
            dust = room[r][c][0] // 5
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                # 유효한 인덱스면 먼지 이동
                if 0 <= nr < R and 0 <= nc < C and room[nr][nc][0] != -1:
                    cnt += 1
                    room[nr][nc][1] += dust
            # 이동하고 남은 먼지양
            room[r][c][0] -= cnt * dust
    # 공기청정기 2칸의 순환 계산
    for i in range(2):
        # 공기청정기 인덱스
        vr, vc = vacuum[i]
        # 위쪽 공기청정기면
        if i == 0:
            # 유효한 행 인덱스
            s = 0
            e = vr + 1
            # 델타 이동 방향
            k = 1
            # 델타 시작점
            d = 0
        else:
            # 유효한 행 인덱스
            s = vr
            e = R
            # 델타 이동 방향
            k = -1
            # 델타 시작점
            d = 2
        dr, dc = delta[d]
        # r, c = 업데이트할 공간
        r, c = vr, vc
        # 업데이트할 공간에 필요한 숫자가 공기청정기가 아니면
        while r + dr != vr or c + dc != vc:
            # 다음 칸이 유효한 인덱스가 아니면 델타 업데이트
            if not (s <= r + dr < e and 0 <= c + dc < C):
                d = (d + k) % 4
                dr, dc = delta[d]
            # 공기청정기에 먼지가 들어오면
            if room[r][c][0] == -1:
                # 남아있는 먼지량에서 빼주기
                total -= sum(room[r+dr][c+dc])
            # 공기청정기로 가는게 아니면
            else:
                # 델타 이동한 다음 칸 먼지 모두 가져오기
                room[r][c][0] = sum(room[r + dr][c + dc])
            # 델타 이동한 칸은 비워주기
            room[r + dr][c + dc] = [0, 0]
            # 업데이트할 공간 업데이트
            r = r + dr
            c = c + dc
        # 다른 곳에서 온 먼지 합쳐주기 ([a, b]에서 b를 a로 몰아주기)
        for r in range(R):
            for c in range(C):
                if room[r][c][0] != -1 and room[r][c][1]:
                    room[r][c][0] += room[r][c][1]
                    room[r][c][1] = 0

print(total)