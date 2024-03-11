import sys
sys.stdin = open('input.txt', 'r')


def check3(lst):
    for node in lst:
        if len(node) != 3:
            return False
    return True


N = int(input())
tree = [[0, 0, 0] for _ in range(N)]
for _ in range(N-1):
    parent, child, value = map(int, input().split())
    tree[child - 1][0] = (parent - 1, value)
    if tree[parent - 1][1] == 0:
        tree[parent - 1][1] = (child - 1, value)
    else:
        tree[parent - 1][2] = (child - 1, value)
print(tree)
for nodes in tree:
    while 0 in nodes:
        nodes.remove(0)
print(tree)
while not check3(tree):
    for idx in range(len(tree)):
        if len(tree[idx]) == 1:
            node, value = tree[idx][0]
            for node1 in tree[node]:
                if node1[0] == node:
                    node1[1] += value
                    break
            tree.pop(idx)
            continue
        elif len(tree[idx]) == 2:
            node1, value1 = tree[idx][0]
            node2, value2 = tree[idx][1]
            for node in tree[node1]:
                if idx == node[0]:
                    tree[node1].remove(node)
                    tree[node1].append((node2, value1 + value2))
                    break
            for node in tree[node2]:
                if idx == node[0]:
                    tree[node2].remove(node)
                    tree[node2].append((node1, value1 + value2))
                    break
            tree.pop(idx)
        continue
