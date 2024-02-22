import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    i = j = 0
    counts = 0
    while i < len(A) and j < len(B):
        if A[i] != B[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == len(B):
            counts += 1
            i = i - j + len(B)
            j = 0
    print(f'#{tc} {len(A)-counts*(len(B)-1)}')
    
