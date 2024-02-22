import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
apart = [[0]* 15 for _ in range(15)]
for i in range(15):
    apart[0][i] = i
for r in range(1, 15):
    for c in range(1, 15):
        apart[r][c] = sum(apart[r-1][:c+1])
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n])