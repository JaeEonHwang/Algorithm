from collections import defaultdict, deque

import sys
sys.stdin = open('input.txt', 'r')

def palindrome(lst):
    ans1 = ""
    ans2 = deque()
    for idx, tpl in enumerate(lst):
        if idx == len(lst) - 1:
            continue
        if tpl[1] % 2:
            return "I'm Sorry Hansoo"
        ans1 += tpl[0] * int(tpl[1]/2)
        ans2.appendleft(str(tpl[0] * int(tpl[1]/2)))
    return ans1 + lst[-1][0] * lst[-1][1] + "".join(ans2)


dct = defaultdict(int)
for i in input():
    dct[i] += 1
srt = sorted(dct.items())
print(palindrome(srt))