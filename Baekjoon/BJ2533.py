import sys
sys.stdin = open('input.txt', 'r')\

def EA(s):
    # dp[s][1] = 1
    for i in sns[s]:
        EA1 = False
        if vstd[i] == 0:
            vstd[i] = 1
            EA(i)

            if i not in ans:
                EA1 = True
        if EA1 and s not in ans:
            ans.append(s)


sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N = int(input())

sns = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    sns[u].append(v)
    sns[v].append(u)
vstd = [0] * (N+1)
vstd[1] = 1
# dp[v][0] = v가 얼리어답터가 아닐 때 자식들 중 얼리어답터의 개수
# dp[v][1] = v가 얼리어답터일 때 자식들 중 얼리어답터의 개수(본인 포함)
# dp = [[0, 0] for _ in range(N+1)]
ans = []
EA(1)
# print(ans)
print(len(ans))