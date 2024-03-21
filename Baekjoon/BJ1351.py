from math import floor


import sys
sys.stdin = open('input.txt', 'r')


N, P, Q = map(int, input().split())
numbers1 = [0 for _ in range(N + 1)]
numbers1[0] = 1
numbers1[1] = 2
i = 1
while i <= N:
    numbers1[i] = numbers1[i//P] + numbers1[i//Q]
    i += 1
print(numbers1)
# print(numbers1[N])
numbers = [0 for _ in range(N + 1)]
numbers[0] = 1
numbers[1] = 2
numbers = [1, 2]
i = 1
pi = 0
qi = 0
numP = 1
numQ = 1
change = [0, 1]
# print('0, 1, ', end="")
while True:
    if i >= N:
        break
    while not (i % P == 0 or i % Q == 0):
        i += 1
    if i % P == 0 and pi + 1 in change:
        pi += 1
    if i % Q == 0 and qi + 1 in change:
        qi += 1
    # print(i, end=", ")
    if (pi in change or qi in change) and (numbers[pi] + numbers[qi]) not in numbers:
    # if (i % P == 0 and pi in change) or (i % Q == 0 and qi in change):
        change.append(i)
        numbers.append(numbers[pi] + numbers[qi])
        # print((i, numbers[i//P] + numbers[i//Q]), end="," )
    # numbers[i] = numbers[pi] + numbers[qi]
    i += 1
print()
print(numbers)
print(change)

# 12 = 6 4
# 14 = 7 4
# 15 = 7 5
# 16 = 8 5
