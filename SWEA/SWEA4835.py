import sys

sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    max_v = 0
    min_v = 10000*N
    arr = list(map(int,input().split()))
    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += arr[i+j]
        if total > max_v:
            max_v = total
        if total < min_v:
            min_v = total
    print(f'#{tc} {max_v-min_v}')