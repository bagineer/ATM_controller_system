from classes import *

if __name__ == '__main__':
    bank = Bank()
    atm = ATM(bank)

    f = open('./testcases.txt', 'r')
    T = int(f.readline())

    for t in range(T):
        print(f'[Test case #{t+1}]')
        N = int(f.readline())

        for n in range(N):
            name, M = f.readline().split()
            client = Client(name)
            bank.add_client(client)

            for m in range(int(M)):
                account_number, account_password, balance, K = f.readline().split()
                account = Account(name, account_number, account_password, int(balance))
                add_account(client, account)
                add_account(bank, account)

                for k in range(int(K)):
                    card_number, pin = f.readline().split()
                    card = Card(card_number, account_number, pin)
                    add_card(account, card)
                    add_card(client, card)
                    add_card(bank, card)

        W = int(f.readline())

        for o in range(W):
            print('='*30)
            print('Please insert your card.')
            input_card_number = f.readline().strip()
            print('- input card number :', input_card_number)
            print()
            searched_card = atm.read_card(input_card_number)
            
            print('Please enter pin number of the card.')
            input_pin = f.readline().strip()
            print('- input pin :', input_pin)
            print()
            is_correct = atm.verify_pin(input_pin)

            if is_correct:
                option = f.readline().split()
                print('- selected option :', option)
                print()
                atm.select_option(*option)
            atm.quit()
            
            print('='*30)
            print()
            print()
    f.close()