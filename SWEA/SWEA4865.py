import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    max_count = 0
    for letter1 in str1:
        count = 0
        for letter2 in str2:
            if letter1 == letter2:
                count += 1
        if count > max_count:
            max_count = count 
    print(f'#{tc} {max_count}')