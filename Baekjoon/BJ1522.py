import sys
sys.stdin = open('input.txt', 'r')

string = input()

# countB = b의 개수
# = b를 모두 연속으로 만들었을 때 연속된 b의 길이
# = a를 모두 연속으로 만들었을 때 연속된 b의 길이
countB = 0
for i in string:
    if i == 'b':
        countB += 1


# b의 개수만큼 연속된 문자열을 검사했을 때
# a가 제일 적게 들어있는 구간에서
# 해당 a를 b로 바꾸면 a, b가 연속으로 이어짐
# 그래서 b의 개수만큼의 구간에서 a가 가장 적게 들어있을 때
# a의 값을 구하면 됨
minA = countB
for i in range(len(string)+countB):
    temp = 0
    for j in range(i, i + countB):
        if string[j % len(string)] == 'a':
            temp += 1
    if temp < minA:
        minA = temp

print(minA)