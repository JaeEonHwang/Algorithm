import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    P, A, B = list(map(int,input().split()))
    A_trial = 0
    B_trial = 0
    l = 1
    r = P

    while True:
        middle = (l + r) // 2
        if middle < A:
            l = middle + 1
            A_trial += 1
        elif middle > A:
            r = middle - 1
            A_trial += 1
        else:
            A_trial += 1
            break
    
    l = 1
    r = P
    while True:
        middle = (l + r) // 2
        if middle < B:
            l = middle + 1
            B_trial += 1
        elif middle > B:
            r = middle - 1
            B_trial += 1
        else:
            B_trial += 1
            break
    
    if A_trial > B_trial:
        print(f'#{tc} B')
    elif A_trial < B_trial:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

        