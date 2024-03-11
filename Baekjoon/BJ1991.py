import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = map(str, input().split())
    tree[parent] = [left, right]
# print(tree)
root = 'A'
# 전위 순회
lst = ['A']
idx = 0
while len(lst) < N:
    left = tree[lst[idx]][0]
    right = tree[lst[idx]][1]
    if left != '.' and left not in lst:
        lst.append(left)
        idx = len(lst) - 1
    elif right != '.' and right not in lst:
        lst.append(right)
        idx = len(lst) - 1
    else:
        idx -= 1
print(''.join(lst))
# 중위 순회
lst = ['A']
idx = 0
while len(lst) < N:
    left = tree[lst[idx]][0]
    right = tree[lst[idx]][1]
    if left != '.' and left not in lst:
        lst.insert(idx, left)
    elif right != '.' and right not in lst:
        idx += 1
        lst.insert(idx, right)
    else:
        idx += 1
print(''.join(lst))
# 후위 순회
lst = ['A']
idx = 0
while len(lst) < N:
    left = tree[lst[idx]][0]
    right = tree[lst[idx]][1]
    if left != '.' and left not in lst:
        lst.insert(idx, left)
    elif right != '.' and right not in lst:
        lst.insert(idx, right)
    else:
        idx += 1
print(''.join(lst))
