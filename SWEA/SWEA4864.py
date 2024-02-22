import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = input()
    M = input()
    start = 0
    while start <= len(M) - len(N):
        if M[start:start+len(N)] == N:
            print(f'#{tc} 1')
            break
        start += 1
    if start > len(M) - len(N):
        print(f'#{tc} 0')