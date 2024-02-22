import sys
sys.stdin = open('input.txt','r')

for _ in range(1, 11):
    tc = int(input())
    maze = [input() for i in range(16)]
    queue = [0] * 16 * 16
    for row in range(16):
        lst = []
        for col in range(16):
            lst.append(int(maze[row][col]))
            if maze[row][col] == '2':
                queue[0] = [row, col]
        maze[row] = lst
    maze[queue[0][0]][queue[0][0]] = 1
    front = -1
    rear = 0
    rdelta = [1, -1, 0, 0]
    cdelta = [0, 0, 1, -1]
    result = False
    while front != rear:
        front += 1
        a = queue[front]
        for i in range(4):
            new_row = a[0] + rdelta[i]
            new_col = a[1] + cdelta[i]
            if maze[new_row][new_col] == 0 and 0 <= new_row <= 16 and 0 <= new_col <= 16:
                rear += 1
                queue[rear] = [new_row, new_col]
                maze[new_row][new_col] = 1
            elif maze[new_row][new_col] == 3:
                result = True
                print(f'#{tc} 1')
                break
    if not result:
        print(f'#{tc} 0')
