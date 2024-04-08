from collections import defaultdict, deque

import sys
sys.stdin = open('input.txt', 'r')

def palindrome(lst):
    # 홀수개인 알파벳이 있다면 무조건 제일 뒤로 가야함
    end = ""
    # 홀수개인 알파벳이 2개 이상이면 팰린드롬 안 되니까 홀수개인 알파벳 세는 용
    endcnt = 0
    # 좌우대칭 중 앞부분
    ans1 = ""
    # 좌우대칭 중 뒷부분
    ans2 = deque()
    for idx, tpl in enumerate(lst):
        # 알파벳이 홀수개면
        if tpl[1] % 2:
            # 카운트 후
            endcnt += 1
            # 홀수개인 알파벳이 2개면 팰린드롬 불가
            if endcnt == 2:
                return "I'm Sorry Hansoo"
            # 한 가운데 알파벳으로 고정
            end = tpl[0]
        # ans1, ans2에 대칭으로 알파벳 넣기
        ans1 += tpl[0] * int(tpl[1]//2)
        ans2.appendleft(str(tpl[0] * int(tpl[1]//2)))
    # 다 합치기
    return ans1 + end + "".join(ans2)


dct = defaultdict(int)
# 알파벳의 개수 세기
for i in input():
    dct[i] += 1
# 알파벳순으로 정렬
srt = sorted(dct.items())
print(palindrome(srt))