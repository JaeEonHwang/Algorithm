import sys
sys.stdin = open('input.txt', 'r')

def preorder(n):
    if n:
        print(n, end = ' ')
        preorder(all[n][0])
        preorder(all[n][1])


V = int(input())
lines = list(map(int, input().split()))
all = [[0, 0, 0] for _ in range(V+1)]

for i in range(int(V-1/2)):
    if all[lines[2 * i]][0] == 0:
        all[lines[2 * i]][0] = lines[2 * i + 1]
    else:
        all[lines[2 * i]][1] = lines[2 * i + 1]
    all[lines[2 * i + 1]][2] = lines[2 * i]

root = 1
while all[root][2] != 0:
    root += 1

preorder(root)
