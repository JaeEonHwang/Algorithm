import sys
sys.stdin = open('input.txt','r')


def bfs(lst):
    temp = []
    for i in lst:
        for j in arr[i]:
            if v[j] == 0:
                v[j] = 1
                temp.append(j)
    if temp:
        bfs(temp)
    else:
        print(f'#{tc} {max(lst)}')
        return

for tc in range(1, 11):
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))
    v = [0] * 101
    v[s] = 1
    arr = [[] for _ in range(101)]
    for i in range(0, n, 2):
        arr[numbers[i]].append(numbers[i + 1])
    bfs([s])