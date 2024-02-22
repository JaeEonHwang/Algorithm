import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = ['0'] * len(string)
    stack[0] = string[0]
    top = 0
    for i in range(1, len(string)):
        if string[i] == stack[top]:
            top -= 1
        else:
            top += 1
            stack[top] = string[i]
    print(f'#{tc} {top+1}')