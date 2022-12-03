from typing import *

class Client:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        self.cards = []


class Account:
    def __init__(self, holder: str, number: str, password: str):
        self.holder = holder
        self.number = number
        self.password = password
        self.cards = []


class Card:
    def __init__(self, client: Client, account: Account, pin: str):
        self.client = client
        self.account = account
        self.pin = pin


class ATM:
    def run(self):
        pass

    def readCard(self, card: Card):
        print("Insert Card")
        pass

    def verifyPIN(self, pin: str):
        pass

    def selectAccount(self):
        pass

    def seeBalance(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass