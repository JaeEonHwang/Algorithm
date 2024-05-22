import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
n = 1
digit = 0
num = 0
while num < K:
    n *= 2
    num += n
    digit += 1
ans = bin(K - num + n - 1)[2:]
ans = ans.replace('0', '4')
ans = ans.replace('1', '7')
ans = (digit - len(ans)) * '4' + ans
print(ans)
