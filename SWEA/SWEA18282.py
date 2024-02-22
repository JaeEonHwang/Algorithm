import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    string = input()
    count1 = 0
    count2 = 0
    for letter in string:
        if letter == '(':
            count1 += 1
        elif letter == ')':
            count2 += 1
        if count2 > count1:
            print(f'#{tc} -1')
            break
    else:
        if count1 == count2:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} -1')
