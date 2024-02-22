import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    for i in range(n//3 + 1):
        # i개의 3과 1로만 이루어진 경우의 수 + i개의 3과 2와 1로 이루어진 경우의 수
        ans += (1 + (n - 3*i) // 2)
    print(ans)