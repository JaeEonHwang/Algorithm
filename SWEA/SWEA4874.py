import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    try:
        stack = []
        for letter in input().split():
            if letter == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif letter == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif letter == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif letter == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            elif letter == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                else:
                    print(f'#{tc} error')
            else:
                stack.append(int(letter))
    except:
        print(f'#{tc} error')
