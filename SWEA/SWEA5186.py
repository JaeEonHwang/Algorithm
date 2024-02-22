import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    jisu = 0.5
    number = 0
    binary = []
    for _ in range(12):
        number += jisu
        if N == number:
            binary.append('1')
            print(f'#{tc} {"".join(binary)}')
            break
        elif N > number:
            binary.append('1')
        else:
            binary.append('0')
            number -= jisu
        jisu *= 0.5
    else:
        print(f'#{tc} overflow')