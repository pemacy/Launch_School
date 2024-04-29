import os

class UtilityMethods:
    BANNER_LENGTH = 40
    SEPARATOR_BAR = '=' * BANNER_LENGTH

    def enter_to_continue(self):
        input('\nPress enter to continue: ')

    def new_line(self):
        print('')

    def clear_screen(self):
        os.system('clear')

    def delay(self, sec):
        os.system(F"sleep {sec}")

    def print_separator_bar(self):
        print(self.__class__.SEPARATOR_BAR)
