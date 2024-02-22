import sys
sys.stdin = open('input.txt', 'r')

pattern = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

T = int(input().strip())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    binary = bin(int(input().strip(), 16))[2:].strip('0')
    while len(binary) % 6:
        binary = '0' + binary
    for i in range(len(binary)//6):
        print(pattern[binary[i*6:i*6+6]], end=' ')
    print()


