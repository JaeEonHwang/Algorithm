import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

try:
    while True:
        map_dict = {}
        for i in range(100):
            map_dict[i] = []

        tc, roads = map(int, input().split())
        road_list = list(map(int, input().split()))

        for path in range(roads):
            map_dict[road_list[path*2]].append(road_list[path*2+1])

        stack = [0]
        top = 0
        while stack[top] != 99:
            try:
                stack.append(map_dict[stack[top]][-1])
                top += 1
            except:
                try:
                    stack.pop()
                    top -= 1
                    map_dict[stack[top]].pop()
                except:
                    print(f'#{tc} 0')
                    break
        else:
            print(f'#{tc} 1')
except:
    pass
