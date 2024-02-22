import sys
sys.stdin = open('input.txt', 'r')


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
tp = t
if w-p < t:
    tp -= (w-p)
    tp %= (2 * w)
    if tp > w:
        tp -= w
    else:
        tp = w - tp
else:
    tp = p + t
tq = t
if h-q < t:
    tq -= (h-q)
    tq %= (2 * h)
    if tq > h:
        tq -= h
    else:
        tq = h - tq
else:
    tq = q + t
print(tp, tq)