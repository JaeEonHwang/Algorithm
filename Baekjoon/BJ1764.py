import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
CL = set()
CS = set()
for i in range(N):
    CL.add(input())
for i in range(M):
    CS.add(input())
CLS = CL.intersection(CS)
CLS = list(CLS)
CLS.sort()
print(len(CLS))
for i in CLS:
    print(i)