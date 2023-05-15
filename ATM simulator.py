 # -*- coding: utf-8 -*-
"""@author:***Lenon***
defaults:
    username:user1
    password:1111
"""
import getpass
 
#the users, their passwords,statements
users=['user1']
passwords=['1111']
amount=[1000]
count=0
#username checker
print("***************************************")
print("*****Welcome to MY ATM simulaor******")
print("***************************************")
while True:
    user=input('Enter username:')
    if user in users:
        if user==users[0]:
         n=0
        elif user==users[1]:
         n=1111
        break    
    else:
     print("invalid Username")
   #password validaton in three attemps
while count < 3:
    password=input('Enter your password:')
    if password.isdigit():
        if user=='user1':
            if password == passwords[0]:
                break
            else:
                count=count+1
                print('Incorrect password')
    else:
        print('password consist of 4 digits')        
if count ==3 :
    print('Three unsucessfull attempts!!')
    print('Your account is temporarily BLOCKED')
    exit()
print("login succesfull")
print(str.capitalize(users[n]),'Welcome to ATM')    
print('******************************************')
print('***********Our Menu***********************')
#Main menu
while True:
    response=input('Select from the following:\nStatements(S)\nWithdraw(w)\nDeposit(d)\nChange pin(p)\nQuit(q)\nType a letter of corresponding option ').lower()
    valid_responses=['s','w','d','p','q']
    response=response.lower()
    if response=='s':
        print(str.capitalize(users[n]),'You have',amount[n],'Euros on your account.')
    elif response=='w' :
        cash_out=int(input('Enter amount to Withdraw:  '))
        if cash_out>=amount[n]:
            print("Cannot perform transaction")
        else:    
           amount[n] = amount[n] - cash_out
        print('Your current balance is: ',amount[n],'Euros')
    elif response=='d':
        cash_in=int(input('Enter amount to deposit: '))
        amount[n] = amount[n] + cash_in
        print('Your new balance is',amount[n],'Euros')
    elif response=='p':
        new_pin=str(getpass.getpass('Enter a new password:'))
        if new_pin.isdigit() and new_pin != passwords and len(new_pin)==4:
             new_ppin=str(getpass.getpass('Confirm new password:'))    
             if new_ppin != new_pin:
                print('PIN MISMACH')
             else:
                password=new_pin
                print('NEW Password SAVED')
        else: 
           print('New password must consist of 4 digits\nAnd should not be similar to previous passwords')
    elif response=='q':
          exit()
    else:
           print('INVALID RESPONSE')