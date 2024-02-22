import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations

N = int(input())
nums = [ i for i in range(1, N+1) ]
# print(nums)
perms = permutations(nums, N)
for perm in perms:
    for num in perm:
        print(num, end=" ")
    print()