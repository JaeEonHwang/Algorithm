import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
parents = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
stack = [1]
while stack:
    parent = stack.pop(0)
    for child in tree[parent]:
        if parents[child] == 0 and child != 1:
            parents[child] = parent
            stack.append(child)
for i in range(2, N + 1):
    print(parents[i])
