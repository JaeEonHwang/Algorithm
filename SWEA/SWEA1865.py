import sys
sys.stdin = open('input.txt', 'r')


def work(n, mul, lst, k):
    global max_v
    if mul < max_v:
        return
    if k == n:
        if mul > max_v:
            max_v = mul
            return
    for i in range(n):
        if i not in lst and arr[k][i] != 0:
            lst.append(i)
            mul *= arr[k][i] / 100
            work(n, mul, lst, k+1)
            mul *= 100 / arr[k][i]
            lst.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    work(N, 100, [], 0)
    print(f'#{tc} {max_v:0.6f}')