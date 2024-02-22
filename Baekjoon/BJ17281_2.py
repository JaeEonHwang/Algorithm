import sys
sys.stdin = open('input.txt', 'r')

import sys
from itertools import permutations
from copy import deepcopy


def max_per_inning(arr):
    arr = deepcopy(arr)
    for i in range(N-1, -1, -1):
        score = 0
        ai = arr[i]
        if sum(ai):
            ai.sort()
            startidx = 0
            for j in range(9):
                if ai[j] != 0:
                    startidx = j
                    break
            cnt0 = 0
            fnhit = ''
            while cnt0 < 3:
                if ai[startidx] == 0:
                    cnt0 += 1
                else:
                    score += 1
                    if ai[startidx] == 4:
                        fnhit = ''
                    else:
                        fnhit += str(ai[startidx])
                startidx = (startidx + 1) % 9
            if fnhit == '':
                pass
            elif fnhit[-1] == '3' or len(fnhit) == 1:
                score -= 1
            elif fnhit[-1] == '2':
                if fnhit[-2] == '1':
                    score -= 2
                else:
                    score -= 1
            else:
                if len(fnhit) == 2:
                    if fnhit[0] == '3':
                        score -= 1
                    else:
                        score -= 2
                else:
                    if fnhit[-3:] == '111':
                        score -= 3
                    elif fnhit[-2] == '3':
                        score -= 1
                    else:
                        score -= 2
        if i == N-1:
            max_score[N-1] = score
        else:
            max_score[i] = score + max_score[i+1]


N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_score = [0] * N
max_per_inning(table)
lineups = permutations((1, 2, 3, 4, 5, 6, 7, 8), 8)
max_v = 0
for lineup in lineups:
    if sum(table[0][1:]) and table[0][lineup[0]] == 0:
        continue
    if max_score[0] == max_v:
        break
    total = 0
    lineup = list(lineup)
    lineup.insert(3, 0)
    idx = 0
    for inning in range(N):
        outcount = 0
        inning_score = 0
        while outcount < 3:
            a = table[inning][lineup[idx]]
            idx = (idx + 1) % 9
            if a == 0:
                outcount += 1
                continue
            inning_score = (inning_score << a) + 2**(a-1)
            total += 1
        if inning_score < 8:
            if inning_score == 0:
                pass
            elif inning_score == 7:
                total -= 3
            elif inning_score == 1 or inning_score == 2 or inning_score == 4:
                total -= 1
            else:
                total -= 2
        else:
            a = bin(inning_score)
            for i in range(-3, 0):
                if a[i] == '1':
                    total -= 1
        if inning < N-1 and total + max_score[inning + 1] < max_v:
            break
    if max_v < total:
        max_v = total
print(max_v)
