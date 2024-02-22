import sys
sys.stdin = open("input.txt", "r")


def number(R, C, lst):
    if len(lst) == 7:
        num = ''.join(lst)
        total.append(num)
        return
    else:
        for dr, dc in delta:
            if 0 <= R + dr < 4 and 0 <= C + dc < 4:
                lst.append(table[R + dr][C + dc])
                number(R + dr, C + dc, lst)
                lst.pop()


T = int(input())
for tc in range(1, T+1):
    table =[list(input().split()) for _ in range(4)]
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    total = []
    for r in range(4):
        for c in range(4):
            number(r, c, [])
    print(f'#{tc} {len(set(total))}')