import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trucks = []
    for _ in range(N):
        trucks.append(list(map(int, input().split())))
    trucks.sort(key=lambda x: x[1])
    use = [trucks[0]]
    for i in range(1,len(trucks)):
        if trucks[i][0] >= use[-1][1]:
            use.append(trucks[i])
    print(f'#{tc} {len(use)}')