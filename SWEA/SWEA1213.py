import sys

sys.stdin = open('input.txt','r',encoding='utf-8')

for T in range(1,11):
    tc = int(input())
    word = input()
    sentence = input()
    count = 0
    
    # for i in range(len(sentence)-len(word)+1):
    #     if sentence[i:i+len(word)] == word:
    #         count += 1 
    # print(f'#{tc} {count}') 

    # for i in range(len(sentence)-len(word)+1):
    #     for j in range(len(word)):
    #         if sentence[i+j] == word[j]:
    #             if j == len(word) - 1:
    #                 count += 1
    #             else:
    #                 continue
    #         else:
    #             break
    # print(f'#{tc} {count}')   

        
    i = 0
    j = 0
    count = 0
    while i < len(sentence) and j < len(word):
        if sentence[i] != word[j]:
            i -= j
            j = -1    
        i += 1
        j += 1
        if j == len(word):
            count += 1
            i -= j
            j = -1
    print(f'#{tc} {count}') 