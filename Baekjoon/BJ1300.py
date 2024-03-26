import sys
sys.stdin = open('input.txt', 'r')


def find_small_num(n):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(n // i, N)
    return cnt


def find_num(n, k):
    cnt = 0
    left = 1
    right = n * n
    while left < right:
        mid = (left + right) // 2
        cnt = find_small_num(mid)
        if cnt < k:
            left = mid + 1
        else:
            right = mid
    return left



N = int(input())
T = int(input())
ans = 0
num = 0
print(find_num(N, T))