T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    min_idx = arr.idex(min(arr))
    max_idx = 0
    for i in range(N):
        if arr[i] >= max_idx:
            max_idx = i

