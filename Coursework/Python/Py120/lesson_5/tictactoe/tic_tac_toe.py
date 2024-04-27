import os
from src.player import Human
from src.player import Computer
from src.board import Board

class TicTacToe:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.board = Board()
        self.current_player = self.human

    def reset_game(self):
        self.clear_screen()
        self.display_welcome()
        self.human.reset()
        self.computer.reset()
        self.current_player = self.human
        self.board.reset()

    def swap_current_player(self):
        if self.current_player is self.human:
            self.current_player = self.computer
        else:
            self.current_player = self.human

    def current_player_move(self):
        self.current_player.move(self.board)

    def play_game(self):
        self.reset_game()
        while not self.is_game_over():
            self.board.display()
            self.current_player_move()
            self.swap_current_player()
            self.clear_screen()
        self.display_results()
        self.play_again()

    def play_again(self):
        if input('Play again? (y/n): ').lower().startswith('y'):
            self.play_game()
        else:
            print('Thank you for playing, goodbye!')

    def is_game_over(self):
        return  self.board.has_winning_combo(self.human) or \
                self.board.has_winning_combo(self.computer) or \
                self.board.is_full()

    def winner(self):
        return self.board.winner(self.human, self.computer)

    def display_welcome(self):
        print('Welcome to Tic Tac Toe!\n')

    def display_results(self):
        print(F"{self.winner()} Won!")

    def clear_screen(self):
        os.system('clear')

# t = TicTacToe()
# t.play_game()
