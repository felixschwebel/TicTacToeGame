import random
from random import randint


class Player:
    def __init__(self, ai_player: bool, board, symbol: str):
        self.ai_player = ai_player
        self.board = board
        self.symbol = symbol

    def check_field(self, field):
        row = round(((field + 1) / 3)) - 1
        column = ((field + 2) % 3) * 2
        if self.board.matrix[row][column] == ' ':
            return row, column
        else:
            return False

    def nonhuman_player(self):
        choice = randint(1, 9)
        while not self.check_field(choice):
            choice = randint(1, 9)
        return self.check_field(choice)

    def human_player(self):
        try:
            choice = int(input('Please choose a field on the board!\n'))
            if choice < 1 or choice > 9:
                raise ValueError
            elif not self.check_field(choice):
                print('Field already occupied, please choose another!')
                self.human_player()
            else:
                return self.check_field(choice)
        except ValueError:
            print('Please put in a valid number!')
            self.human_player()

    def put_stone(self):
        #if AI-Player, put stone automatically
        if self.ai_player:
            field = self.nonhuman_player()
        else:
            field = self.human_player()
        self.board.matrix[field[0]][field[1]] = self.symbol
        self.board.moves += 1
        self.board.show_board()


        #     self.put_stone()

