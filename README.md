# ATM_controller_system

## Overview
This is the simulation of ATM controller system.
<br><br><br>

## classes.py
Classes and functions for ATM controller system.
<br><br>

### \<Classes\>

#### Client
- attributes : name, accounts, cards

#### Account
- attributes : holder, account_number, account_password, balance, cards
- functions
  - get_account_number : return account number.
  - get_holder : return name of account holder.
  - get_account_password : return account password.
  - get_balance : return account balance.
  - deposit : deposit money into account and return balance.
  - withdraw : withdraw moeny from account and return balance.
  
#### Card:
- attributes : card_number, account_number, pin
- functions
  - get_card_number : return card number.
  - get_account_number : return account number.
  - get_pin : return PIN number.
  
#### Bank:
- attributes : clients, accounts, cards, temporary_data
- functions
  - add_client : add client.
  - identify_card : identify card with card number.
  - is_correct_pin : return if PIN number is correct.
  - get_account_balance : get account balance.
  - identify_account : identify account with account number.
  - deposit : deposit money into account.
  - withdraw : withdraw money from account.
  - delete_temporary_data : delete cache data called temporary_data.
  
#### ATM:
- attributes : bank
- functions
  - read_card : read card number.
  - verify_pin : verify if input PIN number is correct.
  - print_options : print work options.
  - select_option : choose an option using integer index number.
  - see_balance : see balance of an account.
  - deposit : deposit money into the account.
  - withdraw : withdraw moeny from the account.
  - quit : quit work.

### \<Functions\>
- add_account : add account into target object.
- add_card : add card into target object.
<br><br><br>

## simulation.py
This is the simulation codes for ATM controller system.

For each test case, execute following processes.<br>

1\. Read card.<br><br>
2\. Enter PIN number.<br><br>
3\. Verify PIN number.<br><br>
4-1\. Select an option if the PIN number is correct.<br><br>
4-2\. Quit work.<br><br>
5\. print message "Thank you."
<br><br><br>

## testcases.txt
First, T is given. T is the number of test cases.

Second, N is given. N is the number of clients.

For N times, the name of client and M are given.<br>
M is the number of accounts that the client has.

For each client, for M times, the account number, account password and K are given.<br>
K is the number of cards that are linked to the account.

For each account, for K times, card number and PIN number are given.<br>

Third, W is given.<br>
W is the number of works.

For W times, card number, PIN number are given.<br>
If the PIN number is correct, the option is given.<br>
the option is consist of integer index number and money can be added into it.
<br><br><br>

## result.txt
This is the result of ATM controller system simulation.
