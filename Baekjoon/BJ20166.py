import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')

def find(god, m, x, y, l):
    global ans
    if god[:l] != m[:l]:
        return
    if len(god) == len(m):
        ans += 1
        return
    delta = ((-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0))
    for dx, dy in delta:
        if arr[(x+dx)%N][(y+dy)%M] == god[l]:
            find(god, m+arr[(x+dx)%N][(y+dy)%M], (x+dx)%N, (y+dy)%M, l + 1)


N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
dic = defaultdict(int)
for _ in range(K):
    ans = 0
    munja = input()
    if dic[munja]:
        print(dic[munja])
    else:
        for x in range(N):
            for y in range(M):
                if arr[x][y] == munja[0]:
                    find(munja, arr[x][y], x, y, 1)
        dic[munja] = ans
        print(ans)
