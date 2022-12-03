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

[Test case #1]
==============================
Please insert your card.
- input card number : 1234-1234-1234-2222

Please enter pin number of the card.
- input pin : 666666

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['1']

You have 100000 won in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 1234-1234-1234-2222

Please enter pin number of the card.
- input pin : 666666

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['2', '5000']

5000 won has been deposited in your account.
Now, you have 105000 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 1234-1234-1234-2222

Please enter pin number of the card.
- input pin : 666666

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['3', '30000']

30000 won has been withdrawn from your account.
Now, you have 75000 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 2222-1234-1111-2222

Please enter pin number of the card.
- input pin : 666666

wrong pin number.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 1234-1234-1234-3333

Please enter pin number of the card.
- input pin : 777777

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['4']

Thank you.
==============================


[Test case #2]
==============================
Please insert your card.
- input card number : 2910-5169-8610-8048

Please enter pin number of the card.
- input pin : 407566

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['1']

You have 100000 won in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 5632-1132-2344-8573

Please enter pin number of the card.
- input pin : 551425

wrong pin number.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 5632-1132-2344-8573

Please enter pin number of the card.
- input pin : 312345

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['3', '2000']

2000 won has been withdrawn from your account.
Now, you have 2998000 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 3254-2233-3245-8233

Please enter pin number of the card.
- input pin : 324623

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['2', '99999999']

99999999 won has been deposited in your account.
Now, you have 100002999 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 3620-7900-2562-2564

Please enter pin number of the card.
- input pin : 308656

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['1']

You have 223000 won in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 3931-6294-9832-9385

Please enter pin number of the card.
- input pin : 844209

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['1']

You have 223000 won in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 5632-1132-2344-8573

Please enter pin number of the card.
- input pin : 123782

wrong pin number.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 3055-3865-2932-8330

Please enter pin number of the card.
- input pin : 076991

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['3', '40000']

40000 won has been withdrawn from your account.
Now, you have -16000 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 8366-8667-5450-9546

Please enter pin number of the card.
- input pin : 771988

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['2', '10000000']

10000000 won has been deposited in your account.
Now, you have 9984000 in your account.
Thank you.
==============================


==============================
Please insert your card.
- input card number : 2910-5169-8610-8048

Please enter pin number of the card.
- input pin : 407566

------------------------------
Please select what you want to do.
1. See Balance.
2. Deposit.
3. Withdraw.
4. Exit
------------------------------
- selected option : ['3', '100000']

100000 won has been withdrawn from your account.
Now, you have 0 in your account.
Thank you.
==============================
