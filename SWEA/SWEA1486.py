import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations


def shelf(heights):
    global min_v
    for i in range(1, N + 1):
        combs = combinations(heights, i)   # 모든 조합 확인
        for comb in combs:
            if sum(comb) >= B:    # 조합의 합과 선반 비교
                if sum(comb) - B < min_v:   # 조합의 합과 최소 차이 비교
                    min_v = sum(comb) - B
                    if min_v == 0:
                        break   # 차이가 0이면 탐색 종료


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_v = 10001
    shelf(heights)
    print(f'#{tc} {min_v}')


