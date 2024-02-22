import sys
sys.stdin = open("input.txt", "r")


def factorial(n):
    global memo
    if n == 1 or n == 0:
        memo[n] = 1
    else:
        memo[n] = n * factorial(n-1)
    return memo[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = [0]*(N+1)
    print(f'#{tc}')
    for i in range(0, N):
        for j in range(0, i+1):
            number = int(factorial(i)/factorial(i-j)/factorial(j))
            print(number, end=' ')
        print()


