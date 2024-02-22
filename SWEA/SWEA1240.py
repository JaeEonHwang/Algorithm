import sys
sys.stdin = open('input.txt', 'r')

# 암호화 규칙 간단하게 만드려고 2진수를 10진수로 바꿈
rule = {0: 13, 1: 25, 2: 19, 3: 61, 4: 35, 5: 49, 6: 47, 7: 59, 8: 55, 9: 11}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 1이 포함되어 있는 행 찾기
    for _ in range(N):
        input1 = input()
        if '1' in input1:
            code_check = input1

    # 해당 행을 뒤에서부터 검색하면서 1이 나오면 56자리를 secret_code로 추출
    secret_code = []
    for i in range(M-1, 0, -1):
        if code_check[i] == '1':
            for j in range(56):
                secret_code.insert(0, code_check[i-j])
            break

    # secret_code에서 7자리씩 추출하면서 10진수로 바꿔준 후 암호화규칙과 일치하면 ans, total에 추가
    # ans = 각 자릿수의 총 합, total = 올바른 암호코드인지 확인용
    total = 0
    ans = 0
    for i in range(8):
        a = int(f"0b{int(''.join(secret_code[7*i:7*i+7]))}", 2)
        for j in range(10):
            if a == rule[j]:
                ans += j
                if i % 2:
                    total += j
                else:
                    total += j * 3
                break

    if total % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')




