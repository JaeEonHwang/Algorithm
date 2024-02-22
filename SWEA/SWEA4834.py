import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(1,T+1):
    tc = input()
    cards = list(map(int,input()))
    cards_set = set(cards)
    frequency = 0
    most_repeated = -1
    for card in cards_set:
        if cards.count(card) > frequency:
            frequency = cards.count(card)
            most_repeated = card
        if cards.count(card) == frequency:
            if most_repeated < card:
                most_repeated = card

    print(f'#{i} {most_repeated} {frequency}')


