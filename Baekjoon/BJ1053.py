import sys
sys.stdin = open('input.txt', 'r')

def palindrome(s):
    opt1 = list(s)
    opt2 = list(s)
    opt2.reverse()
    if opt1 == opt2:
        return True
    else:
        return False
    