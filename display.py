import cards_in_hand
import points


colors = {
    'Clubs': {},
    'Diamonds': {},
    'Hearts': {},
    'Spades': {}
}

for card, priority in cards_in_hand.cards_in_hand.items():
    if 'C' in card:
        colors['Clubs'].update({card: priority})
    elif 'D' in card:
        colors['Diamonds'].update({card: priority})
    elif 'H' in card:
        colors['Hearts'].update({card: priority})
    else:
        colors['Spades'].update({card: priority})

for color, card in colors.items():
    colors[color] = dict(sorted(card.items(), key=lambda item: item[1]['priority'], reverse=True))

for color in colors:
    print(f'{color:<10}', end='\t')
print()

for index in range(max(len(cards) for cards in colors.values())):
    for color, cards in colors.items():
        if index < len(cards):
            card_name = list(cards.keys())[index]
            print(f'{card_name[0]:<10}', end='\t')
        else:
            print(' ' * 10, end='\t')
    print()
print()
print(f"Points: {points.points}")
