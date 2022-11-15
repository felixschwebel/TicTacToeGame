from board import Board
from player import Player

def player(matrix):
    pass


def game():
    game_board = Board()
    print('*******************')
    print('*** TIC TAC TOE ***')
    print('*******************')
    game_board.board_explanation()

    #Let's the user choose the game-mode
    # singleplayer = input('Do you want to play against the Computer? (y/n)\n').lower()
    # if singleplayer == 'y':
    #     #Creates an AI-Player
    #     pass
    # else:
    #     pass
    p1 = Player(True, game_board, 'X')
    name = 'TEST'

    #Check for the game rules
    while game_board.moves < 9:
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

        if over:
            return print('GAME OVER!')

        p1.put_stone()

    return print('Draw!')








game()