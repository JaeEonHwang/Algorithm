import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
line = list(map(int, input().split()))
for i in range(0, N):
    a = line.pop(i)
    line.insert(i-a, str(i+1))
print(' '.join(line))