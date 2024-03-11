import sys
sys.stdin = open('input.txt', 'r')


def empty(lst):
    for i in lst:
        if len(i) > 0:
            return False
    return True


N = int(input())
tree = [set() for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)
# print(tree)
EA = set()
leaf = set()
while len(EA.union(leaf)) != N:

    for idx in range(len(tree)):
        if len(tree[idx]) == 1:
            leaf.add(idx)
            for i in tree[idx]:
                EA.add(i)
    # print(EA)
    # print(leaf)
    for idx in range(1, len(tree)):
        tree[idx] = tree[idx].difference(EA.union(leaf))
    for idx in EA:
        tree[idx] = set()
    # print(tree)
print(len(EA) - 1)


