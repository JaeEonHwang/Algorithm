import sys
sys.stdin = open('input.txt', 'r')

maze = ""
maze = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]
print(maze)