import sys

sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    a = b = c = d = e = 0
    while not num % 2:
        num /= 2
        a += 1
    while not num % 3:
        num /= 3
        b += 1
    while not num % 5:
        num /= 5
        c += 1
    while not num % 7:
        num /= 7
        d += 1
    while not num % 11:
        num /= 11
        e += 1
    print(f'#{tc} {a} {b} {c} {d} {e}')