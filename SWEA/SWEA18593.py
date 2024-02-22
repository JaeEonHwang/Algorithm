import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bit = ''
    print(f'#{tc}',end=' ')
    for _ in range(N):
        bit += input().strip()
    for i in range(int(N*10/7)):
        number = '0b' + bit[i*7:i*7+7]
        print(int(number, 2), end=' ')
    print()
