import sys
sys.stdin = open('input.txt', 'r')


def find_zero(N):
    global total
    global ans

    for i in range(N):
        temp = liquid[i]
        for j in range(i + 1, N):
            temp += liquid[j]
            for k in range(j + 1, N):
                temp += liquid[k]
                if abs(temp) < total:
                    total = abs(temp)
                    ans = [liquid[i], liquid[j], liquid[k]]
                if total == 0:
                    return
                temp -= liquid[k]
            temp -= liquid[j]


N = int(input())
liquid = list(map(int, input().split()))

total = 3000000001
ans = ""
find_zero(N)
print(" ".join(list(map(str, sorted(ans)))))
