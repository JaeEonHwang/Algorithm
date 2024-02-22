import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * 400
    for _ in range(N):
        a, b = map(int, input().split())
        if a < b:
            for i in range((a-1)//2, (b-1)//2+1):
                lst[i] += 1
        else:
            for i in range((b-1)//2, (a-1)//2+1):
                lst[i] += 1
    print(f'#{tc} {max(lst)}')