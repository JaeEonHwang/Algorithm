import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dates = []
flowers = []
for _ in range(N):
    date = list(map(int, input().split()))
    if date[0] < 3 or date[0] == 3 and date[1] == 1:
        flowers.append([date])
    dates.append(date)
dates.sort(key=lambda x: (x[2], x[3]), reverse=True)
print(dates)
print(flowers)
if not flowers:
    print(0)
else:
    while True:
        for flower in flowers:
            idx = 0
            try:
                while flower[-1][2] < dates[idx][0] or (flower[-1][2] == dates[idx][0] and flower[-1][3] + 1 < dates[idx][1]):
                    idx += 1
                    flower.append(dates[idx])
            except:
                pass
            if dates[idx][2] == 12 or (dates[idx][2] == 11 and dates[idx][3] == 30):
                print(len(flower))
                break
        else:
            print()

