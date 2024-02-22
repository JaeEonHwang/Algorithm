import sys
sys.stdin = open("input.txt", "r")


def inorder(n, N):
    global input_num
    if n <= N:
        inorder(n*2, N)
        tree[n] = input_num
        input_num += 1
        inorder(n*2+1, N)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    input_num = 1
    tree = [0] * (N + 1)
    inorder(1, N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
