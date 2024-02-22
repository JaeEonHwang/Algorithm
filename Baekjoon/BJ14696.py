import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
for i in range(N):
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    a = A_list.pop(0)
    b = B_list.pop(0)
    A_list.sort(reverse=True)
    B_list.sort(reverse=True)
    for j in range(max(a, b)+1):
        try:
            if A_list[j] > B_list[j]:
                print('A')
                break
            elif A_list[j] < B_list[j]:
                print('B')
                break
            else:
                continue
        except:
            if a > b:
                print('A')
            elif a < b:
                print('B')
            else:
                print('D')
            break