CARDS_WITH_NO_COLOR = {
    '2': {
        'priority': 0,
    },
    '3': {
        'priority': 1
    },
    '4': {
        'priority': 2
    },
    '5': {
        'priority': 3
    },
    '6': {
        'priority': 4
    },
    '7': {
        'priority': 5
    },
    '8': {
        'priority': 6
    },
    '9': {
        'priority': 7
    },
    'T': {
        'priority': 8
    },
    'J': {
        'priority': 9
    },
    'Q': {
        'priority': 10
    },
    'K': {
        'priority': 11
    },
    'A': {
        'priority': 12
    },
}

COLORS = ['C', 'D', 'H', 'S']

CARDS = {}
for card in CARDS_WITH_NO_COLOR:
    for color in COLORS:
        CARDS[card + ' ' + color] = CARDS_WITH_NO_COLOR[card]
