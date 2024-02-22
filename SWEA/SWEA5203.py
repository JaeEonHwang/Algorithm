import sys
sys.stdin = open("input.txt", "r")


def who_is_winner(cards):
    for i in range(12):
        if i % 2:
            p2.append(cards[i])
            if len(p1) >= 3:
                p2.sort()
                for j in range(len(p2) - 2):
                    if p2[j] == p2[j+2]:
                        return 2
                temp_set = list(set(p2))
                if len(temp_set) >= 3:
                    temp_set.sort()
                    for j in range(len(temp_set) -2):
                        if temp_set[j] == temp_set[j+1] - 1 == temp_set[j+2] - 2:
                            return 2
        else:
            p1.append(cards[i])
            if len(p1) >= 3:
                p1.sort()
                for j in range(len(p1) - 2):
                    if p1[j] == p1[j+2]:
                        return 1
                temp_set = list(set(p1))
                if len(temp_set) >= 3:
                    temp_set.sort()
                    for j in range(len(temp_set) - 2):
                        if temp_set[j] == temp_set[j + 1] - 1 == temp_set[j + 2] - 2:
                            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    c = list(map(int, input().split()))
    p1 = []
    p2 = []
    print(f'#{tc} {who_is_winner(c)}')
