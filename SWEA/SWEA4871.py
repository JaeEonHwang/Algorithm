import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    map_dict = {}
    for i in range(1, V+1):
        map_dict[i] = []
    for i in range(E):
        start, end = map(int, input().split())
        map_dict[start].append(end)
    S, G = map(int,input().split())
    stack = [S]
    top = 0
    while stack[top] != G:
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
    else:
        print(f'#{tc} 1')
