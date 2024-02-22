import sys
sys.stdin = open("input.txt", "r")

    # L = 왼쪽 구간 선택 횟수, R = 오른쪽 구간 선택 횟수
    # l, r = 시작점, 끝점 n = 찾으려고 하는 값
    def binary(lst, l, r, n, L, R):
        if l > r:     # 이진탐색 종료 조건
            return False
        else:
            mid = (l + r) // 2
            if lst[mid] == n:  # 이진탐색 종료 조건
                return True
            else:
                if lst[mid] > n:
                    if L == 0 and R == 0:  # 처음에 왼쪽 구간 선택하는 거면 왼쪽 +2
                        L += 2             # (처음에 2를 더해두면 처음 선택한 구간이)
                    else:                  # (다른 구간의 숫자보다 무조건 높음)
                        L += 1             # 아니면 왼쪽 +1
                    if L > R:              # 처음 선택한 구간이 왼쪽인데
                        if L - R != 2:     # 두 구간의 차가 2가 아니면
                            return False   # 번갈아 선택한 것이 아님
                    elif R > L:            # 처음 선택한 구간이 오른쪽인데
                        if R - L != 1:     # 두 구간의 차가 1이 아니면
                            return False   # 번갈아 선택한 것이 아님
                    else:
                        return False       # 두 구간의 숫자가 같아져도 번갈아 선택한 것이 아님
                    # 통과하면 이진탐색 계속 진행
                    return binary(lst, l, mid - 1, n, L, R)
                else:
                    if L == 0 and R == 0:
                        R += 2
                    else:
                        R += 1
                    if L < R:
                        if R - L != 2:
                            return False
                    elif R < L:
                        if L - R != 1:
                            return False
                    else:
                        return False
                    return binary(lst, mid + 1, r, n, L, R)


    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        A_lst = list(map(int, input().split()))
        A_lst.sort()
        B_lst = list(map(int, input().split()))
        B_lst.sort()
        cnt = 0
        for i in B_lst:
            if binary(A_lst, 0, N-1, i, 0, 0):
                cnt += 1
        print(f'#{tc} {cnt}')