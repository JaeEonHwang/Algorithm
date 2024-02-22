import sys

sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N, numbers = input().split()
    numlist = list(numbers)
    stack = ['a'] * int(N)
    stack[0] = numlist[0]
    top = 0
    for i in range(1, int(N)):
        if numlist[i] != stack[top]:
            top += 1
            stack[top] = numlist[i]
        else:
            top -= 1

    print(f'#{tc}', end=' ')
    for idx in range(top+1):
        print(stack[idx], end='')
    print()