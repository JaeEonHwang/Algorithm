import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()
ans = 1
tape = leaks[0]
for leak in leaks:
    if leak < tape + L:
        continue
    tape = leak
    ans += 1
print(ans)
