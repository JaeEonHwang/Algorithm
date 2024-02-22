import sys
sys.stdin = open('input.txt', 'r')

T = int(input().strip())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    binary = ''
    for letter in input():
        for i in range(3, -1, -1):
            binary += ('1' if int(letter, 16) & 1 << i else '0')
    i = 0
    try:
        while True:
            print(int(binary[7 * i: 7 * (i + 1)], 2), end=' ')
            i += 1
    except:
        print()


