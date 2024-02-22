import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
weather = list(map(int, input().split()))
lst = [-100 * K] * (N-K + 1)
lst[0] = sum(weather[:K])


for i in range(1, N-K + 1):
    lst[i] = lst[i-1] - weather[i-1] + weather[i+K-1]

print(max(lst))
