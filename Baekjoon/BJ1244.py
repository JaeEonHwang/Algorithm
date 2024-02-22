import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, number = list(map(int, input().split()))
    if gender == 1:
        for i in range(1, N+1):
            if not i % number:
                if switch[i-1] == 1:
                    switch[i-1] = 0
                else:
                    switch[i-1] = 1
    else:
        delta = 0
        for i in range(1, N):
            if 0 <= number-1-i and number-1+i < N and switch[number-1-i] == switch[number-1+i]:
                delta += 1
            else:
                break
        if switch[number-1] == 1:
            switch[number-1] = 0
        else:
            switch[number-1] = 1
        for i in range(1, delta+1):
            if switch[number-1-i] == 1:
                switch[number-1-i] = 0
                switch[number-1+i] = 0
            else:
                switch[number-1-i] = 1
                switch[number-1+i] = 1
for i in range(len(switch)):
    if not (i+1)%20:
        print(switch[i])
    else:
        print(switch[i], end=' ')