import sys
sys.stdin = open('input.txt', 'r')


def find_maxidx(lst, n):
    maxidx = n+1
    max_v = -1
    for a in range(n+1, len(lst)):
        if lst[a] >= max_v:
            max_v = lst[a]
            maxidx = a
    return maxidx


T = int(input())
for tc in range(1, T + 1):
    number, trial = input().strip().split()
    trial = int(trial)
    num = []
    for i in number:
        num.append(int(i))
    for i in range(trial):
        for j in range(len(num)-1):
            max_idx = find_maxidx(num, j)
            if num[j] >= num[max_idx]:
                continue
            else:
                if num.count(num[max_idx]) > 1:
                    temp = num[j:j+min(num.count(num[max_idx]), trial-i-1) + 1]
                    temp.sort()
                    for k in range(len(temp)):
                        num[j+k] = temp[k]
                num[j], num[max_idx] = num[max_idx], num[j]
                break
        else:
            num_set = set(num)
            if len(num) == len(num_set) and len(num) != 1:
                num[-1], num[-2] = num[-2], num[-1]
    print(f'#{tc} {"".join(list(map(str,num)))}')
