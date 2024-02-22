import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    for i in range(2**N):
        total = 0
        for j in range(N):
            if 1 << j & i:
                total += numbers[j]
        if total == K:
            cnt += 1
    print(f'#{tc} {cnt}')