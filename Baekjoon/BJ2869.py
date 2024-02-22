import sys
sys.stdin = open('input.txt', 'r')


from math import ceil

A, B, V = map(int, input().split())
d = ceil((V - A) / (A - B)) + 1
print(d)
