from collections import defaultdict

import sys
sys.stdin = open('input.txt', 'r')


def palindrome(flt):
    maxrng = min(flt - 1, len(numbers) - flt)
    if (flt * 2) % 2:
        rng = 0.5
        rng2 = binary(maxrng, 0, flt - 0.5, flt + 0.5)
    else:
        rng = 0
        rng2 = binary(maxrng, 0, flt, flt)
    while flt + rng <= E and flt - rng >= S and numbers[int(flt + rng - 1)] == numbers[int(flt - rng - 1)]:
        rng += 1
    print(rng, rng2)
    return rng


def binary(mxr, mnr, c1, c2):
    if mxr == mnr:
        return mxr
    mid = (mxr + mnr)//2
    opt1 = numbers[c1-mid:c1+1]
    opt2 = list(numbers[c2:c2+mid+1])
    opt2.reverse()
    opt2 = "".join(opt2)
    if opt1 == opt2:
        binary(mxr, mid, c1, c2)
    else:
        binary(mid, mnr, c1, c2)



dct = defaultdict(int)
N = int(input())
numbers = "".join(input().split())
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if S == E:
        # print("1")
        continue
    if dct[(E+S)/2] == 0:
        dct[(E+S)/2] += palindrome((E+S)/2)
    if E - (E+S)/2 <= dct[(E+S)/2]-1:
        # print("1")
        pass
    else:
        # print("0")
        pass
