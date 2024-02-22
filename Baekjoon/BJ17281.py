import sys
sys.stdin = open('input.txt', 'r')

# 순열 생성 외부 라이브러리
from itertools import permutations


# 각 이닝에 최대로 얻을 수 있는 점수를 대략적으로 계산해서 max_per_inning 리스트에 넣음
# 나중에 순열 순환할 때 시간 줄일 수 있음
def max_per_inning(arr):
    for i in range(N-1, -1, -1):   # 이닝은 뒤에서부터 계산
        score = 0
        for j in arr[i]:
            if j != 0:            # 일단 안타 하나당 1점씩 추가
                score += 1
        if arr[i].count(0) == 1:    # 해당 이닝에 아웃당하는 사람이 1명이면 타순 사이클이 3번 돎.
            score *= 3
        elif arr[i].count(0) == 2:  # 해당 이닝에 아웃당하는 사람이 2명이면 타순 사이클이 2번 돎.
            score *= 2
        if max(arr[i]) == 3 or max(arr[i]) == 2:  # 해당 이닝에 제일 긴 장타가 2루타나 3루타면 적어도 1명 남는 주자가 있기 때문에
            score -= 1                            # 1점 빼줌
        elif max(arr[i]) == 1:                    # 해당 이닝에 1루타 밖에 없으면 주자가 3명 남아있음
            score -= 3
        if score < 0:        # 빼줬는데 음수면 득점은 0점
            score = 0
        if i == N-1:
            max_score.insert(0, score)     # max_score[inning] = 해당 이닝부터 원하는 대로 타선을 바꿀 때 낼 수 있는 최대 점수
        else:
            max_score.insert(0, score + max_score[0])


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
max_score = []
max_per_inning(table)
players = (1, 2, 3, 4, 5, 6, 7, 8)    # 1번(인덱스 0번)은 4번타자 고정이기 때문에 8개 숫자로 순열 조합
lineups = list(permutations(players, 8))
max_v = 0
for lineup in lineups:
    total = 0   # 해당 라인업으로 얻는 점수
    lineup = list(lineup)
    lineup.insert(3, 0)    # 4번타순은 1번
    idx = 0
    for inning in range(N):
        base = [0] * 4    # [1] = 1루, [2] = 2루, [3] = 3루, [0] = 홈(점수)
        count0 = 0        # 아웃카운트
        while count0 < 3:  # 아웃카운트 3개 될 때까지 이닝 진행
            if table[inning][lineup[idx]] == 0:    # 0이면 아웃카운트 1 증가
                count0 += 1
            elif table[inning][lineup[idx]] == 1:   # 1루타면 한 칸씩 미룸
                if base[3] == 1:
                    base[0] += 1
                base[3], base[2] = base[2], base[1]
                base[1] = 1
            elif table[inning][lineup[idx]] == 2:   # 2루타면 두 칸씩 미룸
                if base[3] == 1:
                    base[0] += 1
                if base[2] == 1:
                    base[0] += 1
                base[3], base[2] = base[1], 1
                base[1] = 0
            elif table[inning][lineup[idx]] == 3:   # 3루타면 세 칸씩 미룸
                if base[3] == 1:
                    base[0] += 1
                if base[2] == 1:
                    base[0] += 1
                if base[1] == 1:
                    base[0] += 1
                base[3], base[2], base[1] = 1, 0, 0
            elif table[inning][lineup[idx]] == 4:  # 홈런이면 다 비우고 주자 + 1 만큼 점수 더하기
                if base[3] == 1:
                    base[0] += 1
                if base[2] == 1:
                    base[0] += 1
                if base[1] == 1:
                    base[0] += 1
                base[0] += 1
                base[3], base[2], base[1] = 0, 0, 0
            idx = (idx + 1) % 9
        total += base[0]      # base[0] = 해당 이닝에서 얻은 점수
        if inning < N-1 and total + max_score[inning + 1] < max_v:
            break     # 순열 순회 빨리 하기 위한 조건, 앞으로 이닝당 최고점수만큼 얻어도 max 값보다 작으면 해당 라인업 확인 그만
    if max_v < total:
        max_v = total
print(max_v)