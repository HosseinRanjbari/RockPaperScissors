GAME_CHOICES = ('r', 'p', 's')
"""
r : represent Rock
p : represent Paper
s : represent Scissors
"""


# rules of this game base on user and system choice
RULES = {
    'rr': 'draw the game',
    'rp': 'system winner the game',
    'rs': 'user winner the game',

    'pp': 'draw the game',
    'pr': 'user winner the game',
    'ps': 'system winner the game',

    'ss': 'draw the game',
    'sr': 'system winner the game',
    'sp': 'user winner the game'
}

CONVERT_RESULT = {
    'draw the game': 0,
    'system winner the game': -1,
    'user winner the game': 1
}


score_board = {
    'number_of_user_winner_set_play': 0,
    'number_of_system_winner_set_play': 0
}
