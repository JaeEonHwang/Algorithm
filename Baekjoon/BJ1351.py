from collections import defaultdict

import sys
sys.stdin = open('input.txt', 'r')


def calc(n):
    if n == 0:
        return 1
    if numbers[n//P]:
        n1 = numbers[n//P]
    else:
        n1 = calc(n//P)
        numbers[n//P] = n1
    if numbers[n//Q]:
        n2 = numbers[n//Q]
    else:
        n2 = calc(n//Q)
        numbers[n//Q] = n2

    return n1 + n2

N, P, Q = map(int, input().split())
numbers = defaultdict(int)
numbers[0] = 1
print(calc(N))