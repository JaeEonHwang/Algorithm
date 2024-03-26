from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

dict = defaultdict(int)
total = 0
try:
    while True:
        tree = input()
        total += 1
        dict[tree] += 1
except:
    sorted_dict = sorted(dict.items())
    for tree, num in sorted_dict:
        # print(tree, round(num/total*100, 4))
        print("%s %.4f" % (tree, num / total * 100))


