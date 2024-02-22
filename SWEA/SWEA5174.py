import sys
sys.stdin = open("input.txt", "r")


def inorder(n):
    global total
    if n:
        inorder(all[n][0])
        total += 1
        inorder(all[n][1])


T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    E_list = list(map(int,input().split()))
    all = [[0, 0, 0] for _ in range(E+2)]
    for i in range(E):
        if all[E_list[2 * i]][0] == 0:
            all[E_list[2 * i]][0] = E_list[2 * i + 1]
        else:
            all[E_list[2 * i]][1] = E_list[2 * i + 1]
        all[E_list[2 * i + 1]][2] = E_list[2 * i]
    total = 0
    inorder(N)
    print(f'#{tc} {total}')