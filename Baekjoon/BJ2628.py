import sys
sys.stdin = open('input.txt', 'r')

width, height = map(int, input().split())
N = int(input())
width_list = [0, width]
height_list = [0, height]
for _ in range(N):
    direction, cut = map(int, input().split())
    if direction == 0:
        height_list.append(cut)
    else:
        width_list.append(cut)
height_list.sort()
width_list.sort()
max_width = 0
max_height = 0
for i in range(1, len(width_list)):
    if width_list[i] - width_list[i-1] > max_width:
        max_width = width_list[i] - width_list[i-1]
for i in range(1,len(height_list)):
    if height_list[i] - height_list[i-1] > max_height:
        max_height = height_list[i] - height_list[i-1]
print(max_height * max_width)