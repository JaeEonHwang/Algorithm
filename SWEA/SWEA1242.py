import sys
sys.stdin = open('input.txt', 'r')


def password_sum(lst):   # lst = 2진수로 표현된 리스트
    global ratio
    temp = []           # 만들어진 숫자를 추가할 리스트
    for j in range(8):  # 8개의 숫자를 만들기 위한 반복
        number = ''
        try:
            for i in range(7):
                number = lst[-1 - ratio * i - 7 * j * ratio] + number    # 뒤에서부터 찾은 비율대로 7자리씩 뽑은 후
            temp.insert(0, secret_code[number])                          # 딕셔너리에서 검색해서 temp 리스트에 추가
        except:        # 에러가 나는 경우 1. 암호코드 딕셔너리에 해당 7자리 숫자가 없는 경우 2. 하나 더 있었던 것 같은데 기억이 안 남
            ratio -= 1                  # 에러가 나면 비율 하나 줄여서 다시 탐색, 모든 암호코드는 8자리이기 때문에 ratio가 1 아래로 떨어질 일은 없음
            return password_sum(lst)
    # 암호코드 찾으면 정상적인지 확인
    my_sum = 0
    for i in range(4):
        my_sum += (temp[2 * i] * 3)
        my_sum += temp[2 * i + 1]
    if my_sum % 10 == 0:
        return sum(temp)
    else:
        return 0


# 암호코드 딕셔너리
secret_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,\
               '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    arr = []

    # arr 만들기, 만약 다음줄의 같은 위치에 있는 숫자와 같으며 0으로 바꾸기
    for row in range(N):
        arr.append(list(input()))
        for col in range(M):
            if row > 0 and arr[row][col] == arr[row-1][col]:
                arr[row-1][col] = '0'

    total = 0  # 정상적인 암호코드가 있을시 값을 더함
    # arr에 있는 각 줄에 대해서
    for row in arr:
        # 0 밖에 없으면 확인 안 함
        if int(''.join(row), 16) != 0:
            # 양쪽 0 없앰
            row = list(''.join(row).strip('0'))
            # 나중에 오류 없애려고 0 하나 추가
            row.insert(0, '0')
            # row에 있는 수를 4자리 2진수로 바꾸기
            binary = []
            for i in row:
                for j in range(3, -1, -1):
                    binary.append('1' if int(i, 16) & 1 << j else '0')

            # 암호코드가 한 줄에 여러개 있을시 반복하기 위함
            while sum(map(int, binary)) != 0:
                # 이진수 오른쪽 0 없애고
                binary = list(''.join(binary).rstrip('0'))
                # 56의 배수가 되도록 앞에 0 추가
                while len(binary) % 56 != 0:
                    binary.insert(0, '0')
                # 해당 2진수가 가질 수 있는 최대의 비율(?) 구하기
                # 후보 1 = 2진수 제일 뒤에 연속해서 나오는 1의 개수
                count1 = 0
                idx1 = -1
                while binary[idx1] == '1':
                    count1 += 1
                    idx1 -= 1
                # 후보 2 = 2진수 길이 / 56
                # 후보 중 작은 값
                ratio = min(count1, len(binary) // 56)
                # 만들어둔 password_sum 함수로 정상적인 암호 코드의 합 total에 더하기
                total += password_sum(binary)
                # 해당 줄에 남아있는 코드가 있는지 확인하기 위해, 확인한 코드는 제거
                del binary[len(binary) - ratio * 56:]
    print(f'#{tc} {total}')




