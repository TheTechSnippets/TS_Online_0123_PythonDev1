import datetime as dt

import authentication.card_auth as ca
import balance.check_balance as cb
import balance.withdraw_balance as wb
import display.display_ops as dp

current_time = dt.datetime.now()
time = current_time.hour

if time < 11:
    dp.display_good_morning()
elif time < 12 and time < 15:
    dp.display_good_afternoon()
else:
    dp.display_good_evening()

print("Insert your card..")
card_details = ca.read_card_details()
user_pin_input = input("\n Please enter your pin : ")

auth_status = ca.auth_card(card_details, user_pin_input)

if auth_status == 'SUCCESS':
    user_select = input("\n Please select what you want to do : \n 1. Withdraw \n 2. Check Balance \n Your option : ")

    if user_select == '2':
        balance = cb.check_balance()
        print("Your balance is : ", balance)
    elif user_select == '1':
        withdraw_amt = input("\n Enter the amount to withdraw :")
        withdraw_status = wb.withdraw_balance(withdraw_amt)
        print(f'Withdrawn of {withdraw_amt} is {withdraw_status}')
    else:
        print("option not available..")

else:
    print("Invalid Pin .. Failed to authorize....")
