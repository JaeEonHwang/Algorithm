import sys
sys.stdin = open("input.txt", "r")


def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rqsts = list(map(int, input().split()))
    p = [i for i in range(N+1)]
    for i in range(M):
        union(rqsts[2 * i], rqsts[2 * i + 1])
    for i in range(N + 1):
        p[i] = find_set(i)
    print(f'#{tc} {len(set(p))-1}')