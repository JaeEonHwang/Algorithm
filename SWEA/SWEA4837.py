import sys
sys.stdin = open("input.txt", "r")

def count1(num):
    count = 0
    for char in bin(num):
        if char == '1':
            count += 1
    return count


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for tc in range(1,T+1):
    N, T = map(int,input().split())
    answer = 0
    for i in range(1<<len(A)):
        if count1(i) == N:
            subset_sum = 0
            for j in range(len(A)):
                if 1<<j & i:
                    subset_sum += A[j]
            if subset_sum == T:
                answer +=1
            
    print(f'#{tc} {answer}')


