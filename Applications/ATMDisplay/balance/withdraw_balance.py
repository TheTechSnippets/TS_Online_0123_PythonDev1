import exception.WithdrawlOperationExceptions as woe


def withdraw_balance(amount):
    print(f"Withdrawing {amount} from you account.. - inprogress")
    if amount % 100 != 0:
        raise woe.AmountNotInMultiplesOfHundred("Entered amount is not in multiples of 100.")
    if amount > 10000:
        raise woe.AmountNotAvailableInAccount("Entered amount is not available in your account")
    print(f"Withdrawing {amount} from you account.. - done")
    return "SUCCESS"
