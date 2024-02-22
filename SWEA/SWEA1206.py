import sys

sys.stdin = open('input.txt','r')

tc_num = 0
for test in range(10):
    tc_num += 1
    tc = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for building_idx, height in enumerate(buildings[2:tc-2]):
        building_idx += 2
        surrounding = [buildings[building_idx-2], buildings[building_idx - 1], buildings[building_idx + 1], buildings[building_idx + 2]]
        if height >= buildings[building_idx-2] and height >= buildings[building_idx - 1]\
            and height >= buildings[building_idx + 1]\
                and height >= buildings[building_idx + 2]:
            highest_2nd = 0
            for surround in surrounding:
                if surround > highest_2nd:
                    highest_2nd = surround
            total += (height - highest_2nd)
        else:
            continue
    print(f'#{tc_num} {total}')