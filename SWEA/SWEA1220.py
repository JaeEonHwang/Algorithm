import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    # 1이 N극, 2가 S극
    # 위가 N극, 아래가 S극
    count1 = 0
    for col in range(N):
        if table[0][col] == '2':
            table[0][col] = '0'
        elif table[0][col] == '1':
            if table[1][col] == '0':
                table[1][col] = '1'
            elif table[1][col] == '2':
                count1 += 1

    for row in range(1, N - 1):
        for col in range(N):
            if table[row][col] == '1':
                if table[row+1][col] == '0':
                    table[row][col] = '0'
                    table[row+1][col] = '1'
                elif table[row+1][col] == '1':
                    table[row][col] = '0'
                else:
                    count1 += 1
            elif table[row][col] == '2':
                if table[row-1][col] == '0':
                    table[row][col] = '0'
                else:
                    if table[row+1][col] == '2':
                        table[row][col] = '0'
                    elif table[row+1][col] == '0':
                        table[row][col] = '0'
                        table[row+1][col] = '2'
    print(f'#{tc} {count1}')
