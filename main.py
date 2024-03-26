import cards
import random


cards_in_hand = set()

while len(cards_in_hand) < 13:
    cards_in_hand.add(random.choice(list(cards.CARDS.keys())))

cards_in_hand_with_priority = {}
for card in cards_in_hand:
    cards_in_hand_with_priority[card] = cards.CARDS[card]


points = 0
colors = {
    'Clubs': {},
    'Diamonds': {},
    'Hearts': {},
    'Spades': {}
}

for card, priority in cards_in_hand_with_priority.items():
    if 'Ace' in card:
        points += 4
    elif 'King' in card:
        points += 3
    elif 'Queen' in card:
        points += 2
    elif 'Jack' in card:
        points += 1

    if 'Clubs' in card:
        colors['Clubs'].update({card: priority})
    elif 'Diamonds' in card:
        colors['Diamonds'].update({card: priority})
    elif 'Hearts' in card:
        colors['Hearts'].update({card: priority})
    elif 'Spades' in card:
        colors['Spades'].update({card: priority})

for color, card in colors.items():
    colors[color] = dict(sorted(card.items(), key=lambda item: item[1], reverse=True))

colors_short = {}

for color, card in colors.items():
    for key, value in card.items():
        if color not in colors_short:
            colors_short[color] = {}
        colors_short[color][key[0]] = value

for color in colors:
    print(f'{color:<10}', end='\t')
print()

for index in range(max(len(cards) for cards in colors_short.values())):
    for color, cards in colors_short.items():
        if index < len(cards):
            card_name = list(cards.keys())[index]
            print(f'{card_name:<10}', end='\t')
        else:
            print(' ' * 10, end='\t')
    print()
print()
print(f"Points: {points}")
