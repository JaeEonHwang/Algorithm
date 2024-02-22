import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    dic = {')': '(', '}': '{', ']': '['}
    code = input()
    stack = [0] * len(code)
    top = 0
    for letter in code:
        if letter in list(dic.values()):
            stack[top] = letter
            top += 1
        elif letter in list(dic.keys()):
            if stack[top-1] == dic[letter]:
                top -= 1
            else:
                print(f'#{tc} 0')
                break
    else:
        if top != 0:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')


