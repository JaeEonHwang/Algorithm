import sys
sys.stdin = open("input.txt", "r")


def my_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


T = int(input())

for tc in range(1,T+1):
    check = 0
    numbers = list(map(int,input().split()))
    for i in range(1,1<<10):
        subset = []
        for j in range(10):
            if i & (1<<j):
                subset.append(numbers[j])
        if my_sum(subset) == 0:
            check = 1
            break
    print(f'#{tc} {check}')
