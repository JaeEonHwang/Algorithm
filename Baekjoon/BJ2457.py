import sys
sys.stdin = open('input.txt', 'r')

days = {1: 31, 2: 28, 3: 31, 4: 40, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
N = int(input())
dates = []
for _ in range(N):
    date = tuple(map(int, input().split()))
    dates.append(date)
dates.sort(key=lambda x: (x[2], x[3]), reverse=True)
start = (3, 1)
ans = 0
print(dates)
while True:
    try:
        idx = 0
        while (dates[idx][0] == start[0] and dates[idx][1] > start[1]) or dates[idx][0] > start[0]:
            idx += 1
        start = (dates[idx][2], dates[idx][3])
        ans += 1
        print(start)
        dates.remove(dates[idx])
        if start[0] == 12:
            print(ans)
            break
    except:
        print(0)
        break
