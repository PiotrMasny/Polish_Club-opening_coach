import cards
import random


cards_in_hand_without_priority = set()

while len(cards_in_hand_without_priority) < 13:
    cards_in_hand_without_priority.add(random.choice(list(cards.CARDS.keys())))

cards_in_hand = {}

for card in cards_in_hand_without_priority:
    cards_in_hand[card] = cards.CARDS[card]
