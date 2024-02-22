import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, d, k, c = map(int, input().split())
# 회전 초밥 저장
sushi = deque()
for _ in range(N):
    dish = int(input())
    sushi.append(dish)
max_v = 0
# N번동안 한 칸씩 회전하면서 (N=접시 개수)
for _ in range(N):
    temp = []
    # 먹은 스시 저장
    for i in range(k):
        temp.append(sushi[i])
    # 보너스 스시 저장
    temp.append(c)
    # set으로 중복 제거 후 개수 확인
    if len(set(temp)) > max_v:
        max_v = len(set(temp))
    # 최대 종류만큼 다 먹었으면 for문 탈출
    # 시간 줄여보려 넣은 건데 별 차이는 없음
    if max_v == d:
        break
    # 회전 초밥 한 칸 돌리기(rotate는 deque에 있는 메서드임)
    sushi.rotate(1)
print(max_v)
