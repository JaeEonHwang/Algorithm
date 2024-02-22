import sys
sys.stdin = open('input.txt', 'r')


from itertools import combinations

# 사다리 내려가는 함수
# a 배열의 s 시작점에서 제일 아래인 h까지 내려갔을 때
# 시작점과 같은 지점이면 True, 다른 지점이면 False 반환
def ladder(a, s, h):
    c = s
    for i in range(h):
        c += a[i][c]
    if c == s:
        return True
    else:
        return False


# 최소로 가로선 필요개수 찾는 함수
def find_min():
    global ans
    # 가로선이 3개보다 많이 필요하면 -1 반환하면 되므로 3까지만 for문 돌림
    # i = 필요한 가로선 개수
    for i in range(4):
        # 찾아놓은 가로선 옵션에서 개수만큼 뽑을 수 있는 경우의 수
        combs = combinations(options,i)
        # 각 경우의 수에 대하여
        for comb in combs:
            # sort 쓰려고 리스트로 바꿈
            # 원래는 튜플로 나옴
            comb = list(comb)
            # 두 가로선이 연결되면 해당 경우의 수는 검사 안 하고 패스
            comb.sort()
            for j in range(i-1):
                if comb[j][1] + 1 == comb[j][1]:
                    break
            # 유효한 조합이면
            else:
                # 가로선 추가
                for r, c in comb:
                    arr[r][c] = 1
                    arr[r][c+1] = -1
                # 모든 시작점에 대해서 ladder 함수 돌리기
                # ladder() = 사다리 탔을 때 시작점과 끝점이 같은지 확인하는 함수
                for k in range(N):
                    # 만약 시작점과 끝점이 다른 지점이 있으면
                    if not ladder(arr, k, H):
                        # 사다리 원대래로 돌려놓고
                        for r, c in comb:
                            arr[r][c] = 0
                            arr[r][c + 1] = 0
                        # break 해서 다음 comb 경우의 수 보기
                        # (for comb in combs로 돌아감)
                        break
                # 만약 모든 지점이 시작점 = 끝점이면
                # (for k in range(N) 에서 break가 안 됐으면)
                else:
                    # ans에 추가된 사다리 개수 저장
                    ans = i
                    return


N, M, H = map(int, input().split())
# 배열 만들기
# arr[r][c] 에는 사다리 이동 방향 들어갈 예정
# ex) arr[r][c] = -1이면 해당 칸에서는 왼쪽으로 이동
# 0이면 아래로, 1이면 오른쪽으로
arr = [[0] * N for _ in range(H)]
# 사다리 정보 받아서 업데이트
for m in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1
# 가로선 추가할 수 있는 지점 찾기
options = []
# 모든 인덱스에 대해서
for c in range(N):
    for r in range(H):
        # 해당 인덱스에 가로선이 없고
        if arr[r][c] == 0:
            # 같은 열 + 다음 행에도 가로선이 없으면
            if c + 1 < N and arr[r][c+1] == 0:
                # 가로선 추가할 수 있는 지점으로 추가
                options.append((r, c))
# 기본값 -1
ans = -1
# 최소 가로선 개수 찾는 함수
find_min()
print(ans)