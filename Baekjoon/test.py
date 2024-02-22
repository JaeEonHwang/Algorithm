from itertools import combinations


def ladder(a, s, h):
    c = s
    for i in range(h):
        c += a[i][c]
    if c == s:
        return True
    else:
        return False


def find_min():
    global ans
    for i in range(4):
        combs = combinations(options,i)
        for comb in combs:
            comb = list(comb)
            comb.sort()
            for j in range(i-1):
                if comb[j][1] + 1 == comb[j][1]:
                    break
            else:
                for r, c in comb:
                    arr[r][c] = 1
                    arr[r][c+1] = -1
                for k in range(N):
                    if not ladder(arr, k, H):
                        for r, c in comb:
                            arr[r][c] = 0
                            arr[r][c + 1] = 0
                        break
                else:
                    ans = i
                    return


N, M, H = map(int, input().split())
arr = [[0] * N for _ in range(H)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1
options = []
for c in range(N):
    for r in range(H):
        if arr[r][c] == 0:
            if c + 1 < N and arr[r][c+1] == 0:
                options.append((r, c))
ans = -1
temp = 0
comb = []
while len(comb) < i:
    for a in range(len(options)):
        if comb[-1] < a:
            comb.append(a)

find_min()
print(ans)