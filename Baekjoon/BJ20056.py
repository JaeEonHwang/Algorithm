import sys
sys.stdin = open('input.txt', 'r')


from heapq import heappush, heappop

N, M, K = map(int, input().split())
delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
arr = [[[] for _ in range(N)] for _ in range(N)]
fires = []  # 파이어볼
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # 파이어볼 리스트에 정보 저장. [행, 열, 질량, 속도, 방향, 같은 칸에 있는 파이어볼 수, 방향 홀짝]
    heappush(fires, [r, c, m, s, d, 1, d % 2])
for _ in range(K):   # K번동안 이동
    temp1 = []       # 이동 후 파이어볼 정보 저장
    for r, c, m, s, d, n, mod in fires:    # 각 파이어볼에 대해서
        nr = (r + s * delta[d][0]) % N     # 이동 후 인덱스
        nc = (c + s * delta[d][1]) % N
        heappush(temp1, [nr, nc, m, s, d, 1, d % 2])
    temp2 = []       # 같은 칸에 있는 파이어볼 합친 후 저장
    for _ in range(len(temp1)):    # 이동한 후의 파이어볼에 대해서
        # heappop을 사용해서 인덱스가 빠른 순서대로 나옴
        r, c, m, s, d, n, mod = heappop(temp1)
        # temp2에 파이어볼이 저장되어 있고, 제일 최근에 저장된 파이어볼이 같은 칸이면
        if temp2 and temp2[-1][0] == r and temp2[-1][1] == c:
            # 질량 & 속도 더해주기, 같은 칸에 있는 파이어볼 수 + 1
            temp2[-1][2] += m
            temp2[-1][3] += s
            temp2[-1][5] += 1
            # 방향의 홀짝이 기존의 것과 다르면 2로 바꾸기
            if temp2[-1][6] != mod:
                temp2[-1][6] = 2
        # temp2에 처음 넣거나, 제일 최근에 저장된 파이어볼과 다른 칸이면 그대로 temp2에 넣기
        else:
            heappush(temp2, [r, c, m, s, d, n, mod])
    temp1 = []     # 한 칸에 여러 파이어볼이 있는 경우 나누고 저장
    for r, c, m, s, d, n, mod in temp2:
        if n > 1:    # 한 칸에 여러 파이어볼이 있으면
            if m//5 == 0:   # 질량이 0이 되면 무시(소멸)
                continue
            else:
                m //= 5     # 질량 업데이트
                s //= n     # 속도 업데이트
                if mod == 2:    # 방향이 모두 홀수 or 짝수였으면 1 or 0, 아니면 2가 됨
                    k = 1
                else:
                    k = 0
                for j in range(4):
                    # 방향 구할 때 k 사용
                    temp1.append([r, c, m, s, 2 * j + k, 1, k])
        # 한 칸에 하나의 파이어볼만 있으면 그대로 저장
        else:
            temp1.append([r, c, m, s, d, n, mod])
    # 다음 for문을 위한 fires 업데이트
    fires = temp1
# K번 이동 후 모든 질량 더하기
total = 0
for i in fires:
    total += i[2]
print(total)