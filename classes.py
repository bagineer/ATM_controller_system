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
    def __init__(self, number: str, account: Account, pin: str):
        self.number = number
        self.account = account
        self.pin = pin


class ATM:
    def __init__(self):
        self.run()

    def _run(self):
        pass

    def run(self):
        print("Please insert your card")

        
        pass

    def readCard(self, card: Card):
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

class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        self.cards = []

    def addClients(self, client: Client):
        self.clients.append(client)

    def makeAccount(self, client: Client, account: Account):
        pass

    def identifyClient(self, client: Client):
        pass

    def identifyAccount(self, account: Account):
        pass