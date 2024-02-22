import sys
sys.stdin = open("input.txt", "r")


def area(k, a, r, c):
    add_list = []
    if k == 0:
        return service_area[k]
    else:
        for i in range(0, k):
            if 0 <= r - i < len(a) and 0 <= c - (k - i) < len(a):
                add_list.append((r - i, c - (k - i)))
            if 0 <= r - (k - i) < len(a) and 0 <= c + i < len(a):
                add_list.append((r - (k - i), c + i))
            if 0 <= r + (k - i) < len(a) and 0 <= c - i < len(a):
                add_list.append((r + (k - i), c - i))
            if 0 <= r + i < len(a) and 0 <= c + (k - i) < len(a):
                add_list.append((r + i, c + (k - i)))
        service_area[k] = area(k-1, a, r, c) + add_list
    return service_area[k]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_K = 2 * (N - 1) + 1
    most_house = 0
    a = 0
    b = 0
    for row in range(N):
        for col in range(N):
            service_area = []
            service_area = [0] * max_K
            service_area[0] = [(row, col)]
            for K in range(0, max_K):
                cost = K * K + (K + 1) * (K + 1)
                profit = 0
                areas = area(K, arr, row, col)
                home = 0
                for house in areas:
                    if arr[house[0]][house[1]] == 1:
                        profit += M
                        home += 1
                if profit - cost >= 0 and home > most_house:
                    most_house = home
    print(f'#{tc} {most_house}')
