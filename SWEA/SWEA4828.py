import sys

sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    max_v = 0
    min_v = 1000000
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N):
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]
    print(f'#{tc} {max_v - min_v}')