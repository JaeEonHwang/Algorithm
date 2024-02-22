import sys
sys.stdin = open('input.txt', 'r')


def jinsu(number, n):
    lst = []
    while number > 0:
        lst.insert(0, str(number % n))
        number //= n
    return ''.join(lst)


def check_difference(num1, num2):
    if len(num1) != len(num2):
        return False
    countd = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            countd += 1
            if countd > 2:
                return False
    if countd == 1:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()
    for i in range(1, len(binary)):
        if binary[i] == '0':
            b = binary[:i] + '1' + binary[i+1:]
        else:
            b = binary[:i] + '0' + binary[i + 1:]
        if check_difference(jinsu(int(b, 2), 3), ternary):
            print(f'#{tc} {int(b,2)}')
            break

