import datetime as dt
import display.display_ops as dp
import balance.check_balance as cb
import balance.withdraw_balance as wb

current_time = dt.datetime.now()
time = current_time.hour

if time < 11:
    dp.display_good_morning()
elif time < 12 and time < 15:
    dp.display_good_afternoon()
else:
    dp.display_good_evening()

user_select = input("\n Please select what you want to do : \n 1. Withdraw \n 2. Check Balance \n Your option : ")

if user_select == '2':
    cb.check_balance()
elif user_select == '1':
    wb.withdraw_balance()
else:
    print("option not available..")
