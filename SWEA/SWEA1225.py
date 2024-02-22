import sys

sys.stdin = open('input.txt','r')

try:
    while True:
        tc = int(input())
        arr = list(map(int,input().split()))
        front = 0
        minus = 1
        while arr[(front+8)%8] > 0:
            if minus%5 == 0:
                arr[front%8] -= 5
            else:
                arr[front%8] -= minus%5
            minus += 1
            if arr[front%8] <= 0:
                arr[front%8] = 0
                break
            front += 1
        print(f'#{tc}', end = ' ')
        for i in range(8):
            print(arr[(front + 1 + i) % 8], end = ' ')
        print()
except:
    pass