import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    if n:
        inorder(all[n][1])
        print(all[n][0], end='')
        inorder(all[n][2])

for tc in range(1, 11):
    print(f'#{tc }', end=' ')
    N = int(input())
    all = [['', 0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        info = list(input().split())
        all[i][0] = info[1]
        for j in range(2, len(info)):
            all[i][j-1] = int(info[j])
    inorder(1)
    print()


