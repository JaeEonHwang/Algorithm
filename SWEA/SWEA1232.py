import sys
sys.stdin = open('input.txt', 'r')


def postorder(n):
    global arr
    lst = ['+', '-', '*', '/']
    if arr[n][0] in lst:
        arr[n][0] = calculate(arr[n][0], postorder(arr[n][1]), postorder(arr[n][2]))
        return arr[n][0]
    else:
        return arr[n][0]


def calculate(a, n1, n2):
    if a == '+':
        return n1 + n2
    elif a == '-':
        return n1 - n2
    elif a == '*':
        return n1 * n2
    elif a == '/':
        return n1 / n2


for tc in range(1, 11):
    N = int(input())
    arr = [[0, 0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        info = list(input().split())
        if info[1] in '+-*/':
            arr[int(info[0])][0] = info[1]
        else:
            arr[int(info[0])][0] = int(info[1])
        for j in range(2, len(info)):
            arr[int(info[0])][j-1] = int(info[j])
    postorder(1)
    print(f'#{tc} {int(arr[1][0])}')

