import sys

sys. stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    stick = 0
    case = input()
    total = 0
    for i in range(len(case)):
        if case[i] == '(':
            if case[i+1] == ')':
                total += stick
            else:
                stick += 1
                total += 1
        else:
            if case[i-1] == ')':
                stick -= 1
    print(f'#{tc} {total}')