import sys

sys.stdin = open('input.txt','r')

for tc in range(1,11):
    length = int(input())
    formula = input()
    new_formula = ''
    stack = []
    for letter in formula:
        if letter == '+':
            if stack:
                while stack:
                    new_formula += stack.pop()
                stack.append(letter)
            else:
                stack.append(letter)
        elif letter == '*':
            if stack:
                while stack and stack[-1] == '*':
                    new_formula += stack.pop()
                stack.append(letter)
            else:
                stack.append(letter)
        else:
            new_formula += letter
    while stack:
        new_formula += stack.pop()
    

    stack = []
    for letter in new_formula:
        if letter == '+':
            stack.append(stack.pop() + stack.pop())
        elif letter == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(letter))
    
    print(f'#{tc} {stack[0]}')