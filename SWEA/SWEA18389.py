import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    print(f'#{tc}',end = ' ')
    stack = []
    for letter in input():
        if letter in '+-/*':
            stack.append(letter)
        else:
            print(letter,end='')
    while stack:
        print(stack.pop(),end = '')
    print()