import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    tree = [0] * (N+1)
    for i in range(1, N+1):
        tree[i] = num_list[i-1]
        while i//2 != 0:
            if tree[i] < tree[i//2]:
                tree[i], tree[i//2] = tree[i//2], tree[i]
                i = i//2
            else:
                break
    total = 0
    while N//2 != 0:
        total += tree[N//2]
        N = N//2
    print(f'#{tc} {total}')
