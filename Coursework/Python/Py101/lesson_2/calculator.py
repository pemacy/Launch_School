'''
calculator.py app
'''

import os
import json

class Calculate:
    def __init__(self):
        self.numbers = []
        self.operation_symbol = None
        with open('./calculator_messages.json', 'r') as file:
            data = file.read()
        self.messages = json.loads(data)
        self.lang = 'en'

    def setup(self):
        self.welcome_screen()
        self.select_language()

    def welcome_screen(self):
        print(self.messages[self.lang]['welcome'])

    def select_language(self):
        lang = input(self.messages[self.lang]['select language'])
        if lang != '1':
            self.lang = 'non en'
        else:
            self.lang = 'en'

    def validate_input(self, num):
        try:
            int(num)
        except ValueError:
            return False
        self.set_variable(num)
        return True

    def set_variable(self, num):
        self.numbers.append(int(num))

    def re_enter_inputs(self):
        print("Invalid inputs, please re-enter")
        self.enter_inputs()

    def enter_inputs(self):
        self.numbers.clear()
        user_input = True
        print(self.messages[self.lang]['enter inputs'])
        while user_input:
            num = input(f"\nEnter num {len(self.numbers) + 1} >> ")
            if num == '.':
                break
            if not self.validate_input(num):
                print('Invalid Input')

    def select_operation(self):
        return input(self.messages[self.lang]['operation list'])

    def operate(self):
        match self.select_operation():
            case '1':
                self.operation_symbol = '+'
                return self.sum_list()
            case '2':
                self.operation_symbol = '-'
                return self.subtract_list()
            case '3':
                self.operation_symbol = '*'
                return self.multiply_list()
            case '4':
                self.operation_symbol = '//'
                return self.divide_list()
            case _:
                print("Invalid option, please try again.\n")
                return False

    def sum_list(self):
        result = 0
        for num in self.numbers:
            result += num
        return result

    def subtract_list(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result

    def multiply_list(self):
        result = 1
        for num in self.numbers:
            result *= num
        return result

    def divide_list(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result //= num
        return result

    def operation_print_out(self):
        for idx, _ in enumerate(self.numbers):
            self.numbers[idx] = str(self.numbers[idx])
        return f" {self.operation_symbol} ".join(self.numbers)

    def run(self):
        keep_running = True

        while keep_running:
            os.system('clear')
            self.setup()
            result = False
            self.enter_inputs()
            while result is False:
                result = self.operate()
            print(f"{self.operation_print_out()} = {result}")
            run_again = input(self.messages[self.lang]['run again'])
            if run_again != 'y':
                keep_running = False

        return result

calc = Calculate()
calc.run()
