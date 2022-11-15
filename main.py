from board import Board
from player import Player

def player(matrix):
    pass


def game():
    new_board = Board()
    print('*******************')
    print('*** TIC TAC TOE ***')
    print('*******************')
    new_board.board_explanation()

    #Let's the user choose the game-mode
    # singleplayer = input('Do you want to play against the Computer? (y/n)\n').lower()
    # if singleplayer == 'y':
    #     #Creates an AI-Player
    #     pass
    # else:
    #     pass

    #Check for the game rules

    p1 = Player(True, new_board, 'X')
    p1.put_stone()




game()