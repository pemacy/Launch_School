class RpsDisplay:
    def display_selections(self):
        print(F"Computer chose {self.computer.selection}")
        print(F"User chose {self.user.selection}")

    def display_results(self):
        self.display_selections()
        self.display_winner()

    def display_winner(self):
        if self.winner:
            print(F"{self.winner} Wins!")
        else:
            print("Tie Game!")
