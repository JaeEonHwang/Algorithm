import sys

sys.stdin = open('input.txt', 'r')

'''
def max_idx(lst):
    idx = 0
    max_v = 0
    for i in range(len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]
            idx = i
    return idx


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    start = 0
    end = N-1
    total = 0
    while start <= end:
        end = max_idx(numbers[start:]) + start
        new_list = []
        for i in range(start,end+1):
            new_list.append(numbers[i])
        for i in range(len(new_list)):
            total += (new_list[-1] - new_list[i])
        start = end + 1
        end = N - 1
    print(f'#{tc} {total}')
'''
'''
def max_idx(lst,start,end):
    idx = 0
    max_v = 0
    for i in range(start,end):
        if max_v < lst[i]:
            max_v = lst[i]
            idx = i
    return idx


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    start = 0
    total = 0
    while start < N:
        check_list = []
        for idx in range(start,max_idx(numbers,start,N)+1):
            check_list.append(numbers[idx])
        for i in range(len(check_list)):
            total += (check_list[-1] - check_list[i])
        start = max_idx(numbers,start,N) + 1
            
    print(f'#{tc} {total}')
'''
T = int(input())
for tc in range(1, T+1):
    day = int(input())
    arr = list(map(int, input().split()))
    profit = 0                  # 결과 값 - 벌어들인 이득
    max_idx = -1                # 최대값의 인덱스 초기값 인덱스 범위 때문에 -1로 설정함.

    while max_idx+1 != day:
        max_v = 0
        before_max_idx = max_idx            # 전 단계의 최대값 인덱스가 필요해서 저장해놓음
        for i in range(max_idx+1, day):     # max_idx 다음부터의 최대값을 새로 구하기 위한 범위 설정
            if max_v <= arr[i]:             # 최대값 구하기
                max_v = arr[i]
                max_idx = i

        for j in range(max_idx - before_max_idx):           # 새로운 최대값을 구하기 까지의 횟수
            if 0 <= j+before_max_idx+1 < day:               # 인덱스 범위 밖으로 나가는 오류 방지
                profit += max_v - arr[j+before_max_idx+1]   
                # 새로운 최대값에서부터 전 단계의 최대값 사이까지의 인덱스를 각각 새로운 최대값에서 빼주고 더함

    print(f'#{tc} {profit}')