class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg

def withdraw(amount):
    if amount>500:
        raise OverTheLimitException("You can withdraw amount greater than $500 per day.")

withdraw(600)   