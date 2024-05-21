import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
nums = [1]
num = 1
while len(nums) < B:
    num *= 2
    nums = nums + [num] + nums
# print(nums)
print(sum(nums[A:B+1]))
num = 1
ans = B - A + 1
while True:
    if A % (num * 2):
        A += num
    if B % (num * 2):
        B -= num
    if A > B:
        break
    ans += num * ((B - A) / (num * 2) + 1)
    num *= 2
print(int(ans))

# 5 9 : 1 * 5
# 6 8 : 1 * 2
# 8 8 : 2 * 1
# 8 8 : 4 * 1
#
# 25 28 : 1 * 4
# 26 28 : 1 * 2
# 28 28: 2 * 1
print(bin(176+177))