import sys
sys.stdin = open('input.txt', 'r')


from copy import deepcopy

# k세대 커브에 포함된 모든 점 찾는 함수
def dragon(k, lst):
    global g
    if k == g:    # 원하는 세대만큼 찾으면 재귀 종료
        return
    else:
        lst1 = deepcopy(lst)
        er, ec = lst1[-1] # 끝점 인덱스
        temp = []                              # 시작점이 회전이동한 지점이 새로운 끝점이기 때문에
        for i in range(len(lst)-1, -1, -1):    # 항상 끝점을 제일 뒤에 두려고 역순으로 for문 돌림
            tr = er - (ec - lst[i][1])     # 점a가 회전 이동한 후의 인덱스 규칙
            tc = ec + (er - lst[i][0])     # 새로운 x좌표 = 이전 세대 끝점 x 좌표 - (이전 세대 끝점 y좌표 - 점a y좌표)
            temp.append([tr, tc])          # 새로운 y좌표 = 이전 세대 끝점 y좌표 + (이전 세대 끝점 x좌표 - 점a x좌표)
        for i in temp:
            if i not in lst:
                lst.append(i)              # 이미 체크된 점이 아니면 추가
        dragon(k+1, lst)                   # 원하는 단계까지 재귀

# 0세대 커브 찾는 함수
def curve0(r, c, n):
    sr = r
    sc = c
    if n == 0:
        sc += 1
    elif n == 1:
        sr -= 1
    elif n == 2:
        sc -= 1
    else:
        sr += 1
    return [sr, sc]


N = int(input())
all = []
cnt = 0
for i in range(N):
    c, r, d, g = map(int, input().split())
    dots = [[r, c]]
    dots.append(curve0(r, c, d))  # 만들어둔 curve0 함수로 0세대 커브 찾음
    dragon(0, dots)
    for j in dots:
        if j not in all:
            all.append(j)
for r, c in all:
    if [r, c+1] in all and [r+1, c] in all and [r+1, c+1] in all:
        cnt += 1
print(cnt)