import sys
sys.stdin = open('input.txt', 'r')


def my_sum_left(arr, idx):
    global total
    if arr:
        local_max_idx = arr.index(max(arr))
        total += max(arr) * (idx - local_max_idx)
        arr1 = arr[:local_max_idx]
        my_sum_left(arr1, local_max_idx)


def my_sum_right(arr):
    global total
    if arr:
        local_max_idx = arr.index(max(arr))+1
        total += max(arr) * local_max_idx
        arr2 = arr[local_max_idx:]
        my_sum_right(arr2)


N = int(input())
idx_check = []
info = []
for _ in range(N):
    idx, height = map(int, input().split())
    idx_check.append(idx)
    info.append([idx, height])
max_idx = max(idx_check)

ARR = [0] * (max_idx + 1)
for i in info:
    ARR[i[0]] = i[1]

total = max(ARR)
max_idx = ARR.index(max(ARR))
my_sum_left(ARR[:max_idx], max_idx)
my_sum_right(ARR[max_idx+1:])

print(total)

