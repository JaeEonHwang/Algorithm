import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1,T+1):
    N = int(input())
    place_where_bus_stops = []
    for bus in range(N):
        busA, busB = list(map(int,input().split()))
        for i in range(busA,busB+1):
            place_where_bus_stops.append(i)
    P = int(input())
    result = [0] * P
    for i in range(P):
        a = int(input())
        for busstop in place_where_bus_stops:
            if a == busstop:
                result[i] += 1
    print(f'#{tc}', end = ' ')
    for i in result[:P-1]:
        print(f'{i}', end = ' ')
    print(result[-1])