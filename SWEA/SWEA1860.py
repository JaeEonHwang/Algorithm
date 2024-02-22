import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    timeline = [0] * (max(customers)+1)
    for i in range(M, len(timeline), M):
        timeline[i] = K
    for customer in customers:
        if sum(timeline[:customer + 1]) < 1:
            print(f'#{tc} Impossible')
            break
        else:
            timeline[customer] -= 1
    else:
        print(f'#{tc} Possible')

