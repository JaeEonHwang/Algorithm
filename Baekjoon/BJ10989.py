import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
nums = ['10001']
for i in range(N):
    num = int(input())

        if int(nums[j]) >= num:
            nums.insert(j, str(num))
            break
nums.pop()
print('\n'.join(nums))