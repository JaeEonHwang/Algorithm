import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    load = list(map(int, input().split()))
    cargo.sort(reverse=True)
    load.sort(reverse=True)
    total = 0
    start = 0
    for i in load:
        for j in range(start, len(cargo)):
            if i >= cargo[j]:
                total += cargo[j]
                start = j+1
                break
    print(f'#{tc} {total}')