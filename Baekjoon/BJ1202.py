import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    jewels.append(tuple(map(int, input().split())))
jewels.sort(key=lambda x:(x[1], x[0]))
weight = '0'
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()
for i in range(N-1):
    weight += str(i) * (jewels[i+1][0] - jewels[i][0])
visited = 0
steal = 0
s = 0
for bag in bags:
    if bag >= len(weight):
        jewel = N-1
    else:
        jewel = int(weight[bag])
    while ((1 << jewel) & visited) and jewel >= 0:
        jewel -= 1
        if jewel == -1:
            break
    else:
        steal += jewels[jewel][1]
        visited = (1 << jewel) | visited
print(steal)
