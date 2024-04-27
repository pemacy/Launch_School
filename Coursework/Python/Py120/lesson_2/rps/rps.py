import os
import rps_players
from rps_display import RpsDisplay

class RPS(RpsDisplay):
    def __init__(self):
        self._computer = rps_players.Computer()
        self._user = rps_players.User()
        self._winner = None

    @property
    def user(self):
        return self._user

    @property
    def computer(self):
        return self._computer

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner):
        self._winner = winner

    def compare(self):
        if self.computer > self.user:
            self.winner = self.computer
        elif self.user > self.computer:
            self.winner = self.user
        else:
            self.winner = None


    def play(self):
        os.system('clear')
        self.computer.move()
        self.user.move()
        self.compare()
        self.display_results()
        while True:
            if input('\nPlay Again? ') in 'Yy':
                self.play()
            break

rps = RPS()
rps.play()
