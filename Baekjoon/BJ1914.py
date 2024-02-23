import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations


def isclose(comb):
    # DFS, BFS로 완전탐색하기
    v = [0] * 7
    v[0] = 1
    queue = [0]
    while queue:
        A = queue[0]
        for B in range(7):
            if ((comb[A] // 5 == comb[B] // 5 and abs(comb[A]-comb[B]) == 1) or abs(comb[A]-comb[B]) == 5) and v[B] == 0:
                v[B] = 1
                queue.append(B)
        queue.pop(0)
    if 0 in v:
        return False
    else:
        return True


seats = ""
for i in range(5):
    seats += input()

nums = [ i for i in range(0,25)]
combs = combinations(nums, 7)
ans = 0
for comb in combs:
    if isclose(comb):
        Y = 0
        for num in comb:
            if seats[num] == 'Y':
                Y += 1
        if Y < 4:

            ans += 1
print(ans)