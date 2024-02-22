import sys
sys.stdin = open('input.txt', 'r')


def tournament(lst, start, end):
    if start == end:
        return lst[start]
    else:
        middle = (start + end) // 2
        a = tournament(lst, start, middle)
        b = tournament(lst, middle + 1, end)
        if a[0] == b[0]:
            return a
        else:
            if a[0] == 2 or b[0] == 2:
                if a[0] > b[0]:
                    return a
                else:
                    return b
            else:
                if a[0] > b[0]:
                    return b
                else:
                    return a


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    for i in range(len(cards)):
        cards[i] = (cards[i], i + 1)
    print(f'#{tc} {tournament(cards,0,N-1)[1]}')



