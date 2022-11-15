from board import Board
from player import Player


def game():
    #Initializes Board
    game_board = Board()
    print('*******************')
    print('*** TIC TAC TOE ***')
    print('*******************')
    game_board.board_explanation()

    #Initializes Players
    players = [Player(False, game_board, 'X')]

    # let the user choose the game-mode
    single_player = ""
    while single_player != 'y' and single_player != 'n':
        single_player = input('Do you want to play against the Computer? (y/n)\n').lower()
        if single_player == 'y':
            #Creates an AI-Player
            players.append(Player(True, game_board, 'O'))
        elif single_player == 'n':
            players.append(Player(False, game_board, 'O'))
        else:
            print("Please answer with 'y' or 'n'.")

    while game_board.moves < 9:
        for player in players:
            #Checks for game rules
            over = False

            #Check horizontal
            for row in game_board.matrix:
                if row[0] == row[2] == row[4] != ' ':
                    over = True

            #Check vertical
            for i in range(0, 5, 2):
                if game_board.matrix[0][i] == game_board.matrix[1][i] == game_board.matrix[2][i] != ' ':
                    over = True

            #Check diagonal
            if game_board.matrix[0][0] == game_board.matrix[1][2] == game_board.matrix[2][4] != ' ':
                over = True
            elif game_board.matrix[0][4] == game_board.matrix[1][2] == game_board.matrix[2][0] != ' ':
                over = True

            #Check if there is an empty field left
            if game_board.moves == 9:
                return print('Draw!')

            if over:
                if player.symbol == 'X':
                    if single_player == 'y':
                        return print('Computer wins!')
                    else:
                        return print('"O" wins!')
                else:
                    return print('"X" wins!')

            else:
                player.put_stone()

    return print('Draw!')


game_is_on = True
while game_is_on:
    game()
    print('\n####################################\n')
    another_game = input("Press any key for another round of TicTacToe!")
    if another_game == '':
        game_is_on = False
    print('\n####################################\n')