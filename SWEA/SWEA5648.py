import sys

sys. stdin = open('input.txt', 'r')


from heapq import heappop, heappush

T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    atoms = []
    for _ in range(N):
        atom = list(map(int, input().strip().split()))
        atoms.append(atom)
    v = [2002] * N
    exp = []
    delta = ((0, 1), (0, -1), (-1, 0), (1, 0)) #상하좌우 xy
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, d1, K1 = atoms[i]
            x2, y2, d2, K2 = atoms[j]
            dist = (abs(x1 - x2) + abs(y1 - y2)) / 2
            nx1 = x1 + dist * (delta[d1][0])
            ny1 = y1 + dist * (delta[d1][1])
            nx2 = x2 + dist * (delta[d2][0])
            ny2 = y2 + dist * (delta[d2][1])
            if nx1 == nx2 and ny1 == ny2:
                heappush(exp, (dist, i, j))
    for _ in range(len(exp)):
        dist, i, j = heappop(exp)
        if v[i] >= dist and v[j] >= dist:
            v[i] = dist
            v[j] = dist
    total = 0
    for i in range(N):
        if v[i] != 2002:
            total += atoms[i][3]
    print(f'#{tc} {total}')
