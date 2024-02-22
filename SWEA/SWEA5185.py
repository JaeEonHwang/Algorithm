import sys
sys.stdin = open("input.txt", "r")

alphabet = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T+1):
    N, number = input().split()
    print(f'#{tc}', end=' ')
    for letter in number:
        try:
            a = bin(int(letter))[2:]
            while len(a) < 4:
                a = '0' + a
            print(a, end='')
        except:
            print(bin(alphabet[letter])[2:], end='')
    print()
