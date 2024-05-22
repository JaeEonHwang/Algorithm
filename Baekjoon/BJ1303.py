import sys
sys.stdin = open('input.txt', 'r')


def dfs(s, N, M):
    global visited
    global field
    power = 0
    for m in range(M):
        for n in range(N):
            if field[m][n] == s and visited[m][n] == 0:
                visited[m][n] = 1
                soldiers = [(m, n)]
                index = 0
                delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
                while index < len(soldiers):
                    i, j = soldiers[index]
                    for dr, dc in delta:
                        if 0 <= i + dr < M and 0 <= j + dc < N and visited[i + dr][j + dc] == 0 and field[i + dr][j + dc] == s:
                            visited[i + dr][j + dc] = 1
                            soldiers.append((i + dr, j + dc))
                    index += 1
                power += len(soldiers) ** 2
    return power


N, M = map(int, input().split())
field = list(input() for _ in range(M))
visited = [[0] * N for _ in range(M)]
print(field)
print(dfs("W", N, M), dfs("B", N, M))