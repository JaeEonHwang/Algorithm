import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * 2 * N
    for i in range(M):
        leaf, num = map(int, input().split())
        arr[leaf] = num
    for i in range(N - M, 0, -1):
        arr[i] = arr[i*2] + arr[i*2+1]
    print(f'#{tc} {arr[L]}')
