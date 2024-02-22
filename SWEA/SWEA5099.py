import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    # 피자번호: 치즈수 를 딕셔너리로 만듦
    pizza = {0:0}
    for i in range(1, M+1):
        pizza[i] = C[i-1]

    # 화덕에 피자를 채움
    for i in range(N):
        in_progress.append(i+1)

    # 화덕 입구 = start, 화덕 안에서 피자가 도는 거랑 입구가 도는 거랑 상대적으로 보이는 건 같음
    start = 0
    in_progress = []    # 화덕 안에 있는 피자 번호
    cooked = []         # 치즈가 다 녹은 피자 번호
    next_one = N+1
    while len(cooked) < M:
        if pizza[in_progress[start % N]] == 0:
            if in_progress[start % N] != 0:
                cooked.append(in_progress[start % N])
            if next_one > M:
                in_progress[start % N] = 0
            else:
                in_progress[start % N] = next_one
                next_one += 1
        pizza[in_progress[start % N]] //= 2
        start += 1
    print(f'#{tc} {cooked[-1]}')
