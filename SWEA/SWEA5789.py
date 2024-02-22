import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N, Q = map(int,input().split())
    box = ['0'] * N
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            box[j] = str(i)
    print(f'#{tc} {" ".join(box)}')