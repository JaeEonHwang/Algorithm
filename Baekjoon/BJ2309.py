import sys
sys.stdin = open('input.txt', 'r')


from itertools import combinations

height = []
for _ in range(9):
    n = int(input())
    height.append(n)
total = sum(height)
for a, b in combinations(range(9), 2):
    if total - height[a] - height[b] == 100:
        height.pop(b)
        height.pop(a)
        height.sort()
        for i in height:
            print(i)
        break

