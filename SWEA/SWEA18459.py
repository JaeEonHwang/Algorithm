import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int,input().split())
lst = list(map(int,input().split()))
arr = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    arr[lst[i*2]][lst[i*2+1]] = 1
    arr[lst[i*2+1]][lst[i*2]] = 1

queue = [0] * (V)
queue[0] = 1
front = -1
rear = 0
visited = [0] * (V+1)
visited[1] = 1

print('#1 ', end='')
while front != rear:
    front += 1
    a = queue[front]
    print(a, end=' ')
    for i in range(1, V+1):
        if arr[a][i] == 1 and visited[i] == 0:
            rear += 1
            queue[rear] = i
            visited[i] = 1
print()

