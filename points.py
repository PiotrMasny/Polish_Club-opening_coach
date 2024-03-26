import cards_in_hand


points = 0

for card in cards_in_hand.cards_in_hand:
    if 'A' in card:
        points += 4
    elif 'K' in card:
        points += 3
    elif 'Q' in card:
        points += 2
    elif 'J' in card:
        points += 1
