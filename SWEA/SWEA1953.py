import sys
sys.stdin = open("input.txt", "r")


def surround(lst, k):
    global total
    if k == L:
        return
    else:
        temp = []
        for r, c in lst:
            if maps[r][c] == 1:
                for i in range(4):
                    dr = delta[i][0]
                    dc = delta[i][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r+dr][c+dc] in (1, 2, 4, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        elif i == 1:
                            if maps[r+dr][c+dc] in (1, 3, 6, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        elif i == 2:
                            if maps[r+dr][c+dc] in (1, 2, 5, 6) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        elif i == 3:
                            if maps[r+dr][c+dc] in (1, 3, 4, 5) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 2:
                for i in range(2):
                    dr = delta[2 * i][0]
                    dc = delta[2 * i][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r+dr][c+dc] in (1, 2, 4, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r+dr][c+dc] in (1, 2, 5, 6) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 3:
                for i in range(2):
                    dr = delta[2 * i + 1][0]
                    dc = delta[2 * i + 1][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r+dr][c+dc] in (1, 3, 6, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r + dr][c + dc] in (1, 3, 4, 5) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 4:
                for i in range(2):
                    dr = delta[i + 1][0]
                    dc = delta[i + 1][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r + dr][c + dc] in (1, 3, 6, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r + dr][c + dc] in (1, 2, 5, 6) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 5:
                for i in range(2):
                    dr = delta[i][0]
                    dc = delta[i][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r + dr][c + dc] in (1, 2, 4, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r + dr][c + dc] in (1, 3, 6, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 6:
                for i in range(2):
                    dr = delta[- i][0]
                    dc = delta[- i][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r + dr][c + dc] in (1, 2, 4, 7) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r + dr][c + dc] in (1, 3, 4, 5) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            elif maps[r][c] == 7:
                for i in range(2):
                    dr = delta[i+2][0]
                    dc = delta[i+2][1]
                    if 0 <= r + dr < N and 0 <= c + dc < M:
                        if i == 0:
                            if maps[r + dr][c + dc] in (1, 2, 5, 6) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
                        if i == 1:
                            if maps[r + dr][c + dc] in (1, 3, 4, 5) and (r + dr, c + dc) not in temp:
                                temp.append((r + dr, c + dc))
                                total += 1
            maps[r][c] = 0
        a = temp[:]
        surround(a, k+1)


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    queue = [(R, C)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    total = 1
    surround(queue, 1)
    print(f'#{tc} {total}')