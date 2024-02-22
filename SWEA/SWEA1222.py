import sys

sys.stdin = open('input.txt','r')

for tc in range(1,11):
    length = int(input())
    formula = input()
    stack = []
    new_formula = ''
    for letter in formula:
        if letter == '+':
            if not stack:
                stack.append(letter)
            else:
                new_formula += letter
        else:
            new_formula += letter
    new_formula += stack.pop()
    
    stack = []
    for letter in new_formula:
        if letter == '+':
            temp = (int(stack.pop()) + int(stack.pop()))
            stack.append(temp)
        else:
            stack.append(letter)
    print(f'#{tc} {stack[0]}')