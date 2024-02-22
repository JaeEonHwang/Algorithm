import sys

sys.stdin = open('input.txt','r')

num_dict = {'ZRO': 0, 'ONE': 1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN':9}
for i in range(10):
        num_dict[list(num_dict.items())[i][1]] = list(num_dict.items())[i][0]

T = int(input())
for _ in range(1,T+1):
    tc,num= input().split()
    print(tc)
    numbers = list(input().split())
    for i in range(int(num)):
        numbers[i] = num_dict[numbers[i]]
    numbers.sort()
    for i in range(int(num)):
         numbers[i] = num_dict[numbers[i]]
    print(' '.join(numbers))
    