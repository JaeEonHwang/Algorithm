import sys
sys.stdin = open("input.txt", "r")


def find_max(some_list):
    max_num = some_list[0]
    for i in range(len(some_list)):
        if max_num < some_list[i]:
            max_num = some_list[i]
    return max_num


def find_min(some_list):
    min_num = some_list[0]
    for i in range(len(some_list)):
        if min_num > some_list[i]:
            min_num = some_list[i]
    return min_num


for test_case in range(1, 11):
    trial = int(input())
    boxes = list(map(int, input().split()))
    while trial > 0:
        max_idx = boxes.index(find_max(boxes))
        boxes[max_idx] -= 1
        min_idx = boxes.index(find_min(boxes))
        boxes[min_idx] += 1
        trial -= 1
        gap = find_max(boxes)-find_min(boxes)
        if gap < 2:
            break
    print(f'#{test_case} {find_max(boxes)-find_min(boxes)}')

