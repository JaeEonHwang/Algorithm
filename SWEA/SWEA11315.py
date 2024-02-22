import sys
sys.stdin = open('input.txt', 'r')


def find_5mok(lst, n):
    for row in range(n):
        if 'ooooo' in lst[row]:
            return 'YES'
        for col in range(n):
            try:
                if lst[row][col] + lst[row+1][col] + lst[row+2][col] + lst[row+3][col] + lst[row+4][col] == 'ooooo':
                    return 'YES'
            except:
                pass
            try:
                if lst[row][col] + lst[row+1][col+1] + lst[row+2][col+2] + lst[row+3][col+3] + lst[row+4][col+4] == 'ooooo':
                    return 'YES'
            except:
                pass
            try:
                if row >= 4:
                    if lst[row][col] + lst[row-1][col+1] + lst[row-2][col+2] + lst[row-3][col+3] + lst[row-4][col+4] == 'ooooo':
                        return 'YES'
            except:
                pass
    return 'NO'


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {find_5mok(arr,N)}')

