'''
def auth_card(card_number, provider, card_type, pin):
    # do some ops
    return "SUCCESS"
'''


def auth_card(card_details, pin):
    number = card_details.get("number")
    type = card_details.get("type")
    provider = card_details.get("provider")
    return "SUCCESS"


def read_card_details():
    # do internal reading
    return {'number': 12345, 'type': 'VISA', 'provider': "HDFC"}
