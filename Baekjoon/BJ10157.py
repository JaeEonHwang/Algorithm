import sys
sys.stdin = open('input.txt', 'r')

C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
else:
    cp1 = 1
    cp2 = 2 * (C + R) - 4
    sp = 1
    while K > cp2:
        cp1 = cp2 + 1
        C -= 2
        R -= 2
        sp += 1
        cp2 += (2 * (C + R) - 4)
    if K <= cp1 + R - 1:
        print(sp, sp + K - cp1)
    elif cp1 + R <= K <= cp1 + R - 2 + C:
        print(sp + K - cp1 - R + 1, sp + R - 1)
    elif cp1 + R - 1 + C <= K <= cp1 + 2 * R - 3 + C:
        print(sp + C - 1, sp + cp1 + 2 * R - 3 + C - K)
    else:
        print(sp + cp2 - K + 1, sp)
