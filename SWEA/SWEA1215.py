import sys

sys.stdin = open('input.txt','r',encoding='utf-8')

for tc in range(1,11):
    N = int(input())
    arr = [input() for _ in range(8)]
    
    count = 0
    for row in range(8-N+1):
        for col in range(8):
            word = ''
            for i in range(N):
                word += arr[row+i][col]
            if word == word[::-1]:
                count +=1 
    
    for row in range(8):
        for col in range(8-N+1):
            word = ''
            for i in range(N):
                word += arr[row][col+i]
            if word == word[::-1]:
                count +=1 

    print(f'#{tc} {count}') 