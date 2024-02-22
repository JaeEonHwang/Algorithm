import sys
sys.stdin = open('input.txt', 'r')

lst = list(map(int,input().split()))
N = len(lst)

def powerset(idx,N,s):
    global counts
    if s == 10:
        counts += 1
        return
    elif idx == N:
        return
    elif s > 10:
        return
    else:
        powerset(idx+1,N,s)
        powerset(idx+1,N,s+lst[idx])


selected = [0] * 10
counts = 0
idx = 0
powerset(idx,N,0)
print(f'#1 {counts}')