from config import GAME_CHOICES, RULES, CONVERT_RESULT, score_board

from random import sample


# to get a choice from user and validate that choice
def get_user_choice():
    user_input = input("Enter your choice (r, p, s): ")

    if user_input not in GAME_CHOICES:
        print("you should enter a choice among (r, p, s) !")
        return get_user_choice()

    return user_input


# to get a choice from system randomly
def get_system_choice():
    sys_choice = ''.join(sample(GAME_CHOICES, k=1))
    return sys_choice


# to find winner the game
def find_winner(userchoice, systemchoice):
    players_string = userchoice + systemchoice

    result_game = RULES[players_string]

    print("*" * 30)
    print(f"User choice was: {userchoice}")
    print(f"system choice was: {systemchoice}")
    print(f"result this game is: {result_game}")
    print("*" * 30)

    return CONVERT_RESULT[result_game]


# update score board after each set of play
def update_score_board(score_of_players):
    if score_of_players['user_score'] == 3:
        score_board['number_of_user_winner_set_play'] += 1
    else:
        score_board['number_of_system_winner_set_play'] += 1

    print("#" * 60)
    print("result of this set is: ")
    print(f"user: {score_board['number_of_user_winner_set_play']}".rjust(24))
    print(f"system: {score_board['number_of_system_winner_set_play']}".rjust(24))
    print("#" * 60)


# to asking want play again or not
def play_again():
    PLAY_AGAIN_ANSWER = ('y', 'n', 'Y', 'N')

    want_play_again = input("Do you want to play again?(y/n): ")

    if want_play_again not in PLAY_AGAIN_ANSWER:
        print("@" * 30)
        print("you should enter y/Y for want play again")
        print("and")
        print("if you don't want enter n/N")
        print("@" * 30)

        play_again()

    elif want_play_again == 'y' or want_play_again == 'Y':
        play()

    else:
        return


# main play ground
def play():

    player_score = {'user_score': 0, 'system_score': 0}

    while (player_score['user_score'] < 3) and (player_score['system_score'] < 3):
        user_choice = get_user_choice()
        system_choice = get_system_choice()

        winner = find_winner(user_choice, system_choice)

        if winner == -1:
            player_score['system_score'] += 1

        if winner == 1:
            player_score['user_score'] += 1

    update_score_board(player_score)

    play_again()


if __name__ == '__main__':
    play()
