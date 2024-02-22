import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
N = int(input())
stores = []
for _ in range(N):
    a, b = map(int, input().split())
    stores.append((a, b))
start = list(map(int, input().split()))
total = 0
for i in range(N):
    store = stores[i]
    if store[0] == start[0]:
        total += abs(store[1] - start[1])
    else:
