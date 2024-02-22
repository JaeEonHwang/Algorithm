import sys

sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(input().split('0'))
    length = 0
    for i in arr:
        if len(i) > length:
            length = len(i)
    print(f'#{tc} {length}')