from math import comb

import sys
sys.stdin = open('input.txt', 'r')


def prime_score(p):
    chance = 0
    for prime in (2, 3, 5, 7, 11, 13, 17):
        chance_n = (p ** prime) * ((1 - p) ** (18 - prime)) * comb(18, prime)
        chance += chance_n
    return chance


a = int(input())/100
b = int(input())/100
chance_a = prime_score(a)
chance_b = prime_score(b)
print(chance_a + chance_b - chance_b * chance_a)