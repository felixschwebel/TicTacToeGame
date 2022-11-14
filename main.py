from board import Board


def multiplayer(matrix):
    field = int(input('Please choose a field on the board!\n'))
    #Converts the user input into the list entry location
    row = round(((field+1)/3))-1
    column = ((field+2)%3)*2


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

    multiplayer()



game()