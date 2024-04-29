from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
words = set()
prefixes = defaultdict(int)
for _ in range(N):
    word = input()
    # 중복되는 단어는 접두사x 집합에 영향이 없으니까 패스
    if word not in words:
        words.add(word)
        prefix = ""
        # 모든 접두사 저장
        for alphabet in word:
            prefix += alphabet
            prefixes[prefix] += 1

ans = 0
for word in words:
    # 해당 단어가 접두사가 아니라면 사전에 1개만 저장되어있음
    if prefixes[word] == 1:
       ans += 1
print(ans)
