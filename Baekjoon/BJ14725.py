import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
roads = []
for _ in range(N):
    info = list(input().split())
    roads.append(info[1:])
roads.sort()
for i in range(len(roads)):
    if i == 0:
        for j in range(len(roads[i])):
            print("--"*j+roads[i][j])
    else:
        for j in range(len(roads[i])):
            if len(roads[i-1]) > j and roads[i-1][j] == roads[i][j]:
                continue
            for k in range(j, len(roads[i])):
                print("--"*k+roads[i][k])
            break