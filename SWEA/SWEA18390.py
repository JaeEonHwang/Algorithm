import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
for tc in range(1,T+1):
    print(f'#{tc}',end = ' ')
    stack = []
    for letter in input():
        if letter in '+-/*(':
            if not stack:
                stack.append(letter)
            else:
                while icp[letter] <= isp[stack[-1]]:
                    print(stack.pop(),end='')
                stack.append(letter)
        elif letter == ')':
            while stack[-1] != '(':
                print(stack.pop(),end='')
            stack.pop()
        else:
            print(letter,end='')
    while stack:
        print(stack.pop(),end='')
    print()
    