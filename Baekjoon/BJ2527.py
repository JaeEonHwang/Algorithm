import sys
sys.stdin = open('input.txt', 'r')


for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x3 < x1:
        x1, x3 = x3, x1
        y1, y3 = y3, y1
        x2, x4 = x4, x2
        y2, y4 = y4, y2
    if x3 > x2:
        print('d')
    elif x3 == x2:
        if y2 < y3:
            print('d')
        elif y2 == y3:
            print('c')
        else:
            if y1 < y4:
                print('b')
            elif y1 == y4:
                print('c')
            else:
                print('d')
    else:
        if y2 < y3:
            print('d')
        elif y2 == y3:
            print('b')
        else:
            if y1 < y4:
                print('a')
            elif y1 == y4:
                print('b')
            else:
                print('d')



