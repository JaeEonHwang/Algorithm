import sys
sys.stdin = open('input.txt', 'r')

from math import ceil

N, K = map(int, input().split())
stu = [0] * 12
for _ in range(N):
    S, Y = map(int, input().split())
    stu[Y * 2 - 1 - S] += 1
room = 0
for i in range(12):
    room += ceil(stu[i] / K)
print(room)