import sys
import pickle
sys.stdin = open('input.txt', 'r')


def page_sum(x):
    if not tree[x]:
        for i in range(1, x):
            opt1 = page_sum(i)
            opt2 = page_sum(x-i)
            for j in opt1:
                for k in opt2:
                    temp = j + k
                    for l in range(len(temp)):
                        temp[l] += 1
                    tree[x].append(temp)
    return tree[x]


tree = [[] for _ in range(501)]
tree[1] = [[0]]
tree[2] = [[1, 1]]
tree[3] = [[1, 2, 2], [2, 2, 1]]
tree[4] = [[2, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2], [3, 3, 2, 1], [1, 2, 3, 3]]

T = int(input())
page_sum(500)
for _ in range(T):
    K = int(input())
    file = list(map(int, input().split()))
    ans = 10000 * K + 1
    options = page_sum(K)
    for option in options:
        temp = 0
        for i in range(K):
            temp += option[i] * file[i]
        if temp < ans:
            ans = temp
    print(ans)
