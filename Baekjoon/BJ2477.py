import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
direction_info = []
length_info = []
for i in range(6):
    direction, length = map(int, input().split())
    direction_info.append(direction)
    length_info.append(length)
while direction_info.count(direction_info[0]) != 1 or direction_info.count(direction_info[1]) != 1:
    direction_info.insert(0, direction_info.pop())
    length_info.insert(0, length_info.pop())
print((length_info[0] * length_info[1] - length_info[3] * length_info[4]) * K)


