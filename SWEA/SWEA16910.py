import sys
sys.stdin = open("input.txt", "r")

from math import sqrt

T = int(input())
for tc in range(1,T + 1):
    N = int(input())
    total = 0
    for i in range(-N,N+1):
        total += 2 * int(sqrt(N**2 - i**2)) + 1
    print(f'#{tc} {total}')