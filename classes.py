from typing import *

class Client:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        self.cards = []


class Account:
    def __init__(self, holder: str, account_number: str, account_password: str, balance: int):
        self.holder = holder
        self.account_number = account_number
        self.account_password = account_password
        self.balance = balance
        self.cards = []

    def get_account_number(self) -> str:
        return self.account_number

    def get_holder(self) -> str:
        return self.holder
        
    def get_account_password(self) -> str:
        return self.account_password
        
    def get_balance(self) -> str:
        return self.balance

    def deposit(self, money: int) -> int:
        self.balance += money
        return self.balance

    def withdraw(self, money: int) -> int:
        self.balance -= money
        return self.balance


class Card:
    def __init__(self, card_number: str, account_number: str, pin: str):
        self.card_number = card_number
        self.account_number = account_number
        self.pin = pin

    def get_card_number(self) -> str:
        return self.card_number

    def get_account_number(self) -> str:
        return self.account_number

    def get_pin(self) -> str:
        return self.pin


class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        self.cards = []
        self.temporary_data = dict()

    def add_client(self, client: Client):
        self.clients.append(client)

    def identify_card(self, card_number: str):
        for card in self.cards:
            if card_number == card.get_card_number():
                self.temporary_data['card'] = card

        self.identify_account(self.temporary_data['card'].get_account_number())

    def is_correct_pin(self, pin: str) -> bool:
        if pin == self.temporary_data['card'].get_pin():
            return True
        else:
            return False

    def get_account_balance(self):
        return self.temporary_data['account'].get_balance()
            
    def identify_account(self, account_number: str):
        for account in self.accounts:
            if account_number == account.get_account_number():
                self.temporary_data['account'] = account

    def deposit(self, money: int) -> int:
        balance = self.temporary_data['account'].deposit(money)
        return balance

    def withdraw(self, money: int):
        balance = self.temporary_data['account'].withdraw(money)
        return balance

    def delete_temporary_data(self):
        self.temporary_data = dict()


class ATM:
    def __init__(self, bank: Bank):
        self.bank = bank

    def read_card(self, card_number: str):
        self.bank.identify_card(card_number)

    def verify_pin(self, pin: str) -> bool:
        is_correct = self.bank.is_correct_pin(pin)
        if is_correct:
            self.print_options()
        else:
            print("Wrong pin number")
        return is_correct

    def print_options(self):
        print('-'*30)
        print('Please select what you want to do.')
        print('1. See Balance.')
        print('2. Deposit.')
        print('3. Withdraw.')
        print('4. Exit')
        print('-'*30)

    def select_option(self, option: int, money: int = None):
        option = int(option)
        print("select_option :", option, money)
        if option == 1:
            self.see_balance()
        elif option == 2:
            self.deposit(int(money))
        elif option == 3:
            self.withdraw(int(money))
        self.quit()

    def see_balance(self):
        print(f'You have {self.bank.get_account_balance()} won in your account.')

    def deposit(self, money):
        balance = self.bank.deposit(money)
        print(f'{money} won has been deposited in your account.')
        print(f'Now, you have {balance} in your account.')

    def withdraw(self, money):
        balance = self.bank.withdraw(money)
        print(f'{money} won has been withdrawn from your account.')
        print(f'Now, you have {balance} in your account.')

    def quit(self):
        print('Thank you.')
        self.bank.delete_temporary_data()


def add_account(target, account: Account):
    target.accounts.append(account)

def add_card(target, card: Card):
    target.cards.append(card)