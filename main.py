import game
import model


def play_with_terminal():
    model.SHOW_TERMINAL = True
    nb_player = int(input("Number of players"))
    players = []
    nb_ia = 0
    for i in range(nb_player):
        mode = int(input("Ia or human ? (0 IA, 1 human)"))
        if mode == 0:
            players.append(model.AI(nb_ia))
            nb_ia += 1
        else:
            name = input("Name player : ")
            players.append(model.HumanPlayer(name))
    party = game.Game(players)
    while True:
        party.play_round()
        is_empty = party.reset()
        if is_empty:
            print("END OF THE GAME NO MORE PLAYER")
            return
        choice = int(input("Do you want to continue ? (0 Yes, 1 No)"))
        if choice == 1:
            print("END OF THE GAME")
            return


def play_with_pygame():
    import display_function
    model.SHOW_TERMINAL = False
    window, window_height, window_width, white_rect, white_rect_height = display_function.init_display()
    WINDOWS = [window, window_height, window_width, white_rect, white_rect_height]

    list_players = display_function.get_start(WINDOWS)[1]
    nb_ia = 0
    players = []
    for i in range(len(list_players)):
        if len(list_players[i]) == 1:
            players.append(model.AI(nb_ia))
            nb_ia += 1
        else:
            players.append(model.HumanPlayer(list_players[i][1]))
    party = game.Game(players)
    while True:
        party.play_round(WINDOWS)
        is_empty = party.reset(WINDOWS)
        if is_empty:
            0  # display.close_the_game(WINDOWS)
            return
        if 0 == 0:  # display.ask_want_to_continue()(return true or false):
            0  # display.close_the_game(WINDOWS)
            return


if __name__ == "__main__":
    play_with_pygame()
