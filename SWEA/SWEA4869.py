import sys
sys.stdin = open('input.txt', 'r')

def box(n):
    b = [0] * (n+1)
    b[1] = 1
    b[2] = 3
    for i in range(3,n+1):
        b[i] = b[i-1] + b[i-2] * 2

    return b[n]


T = int(input())
for tc in range(1,T+1):
    N = int(int(input())/10)
    print(f'#{tc} {box(N)}')