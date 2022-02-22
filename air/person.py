from wallet import Wallet

class Person:
    def __init__(self):
        self._wallet = Wallet()
    
    def get_wallet(self):
        return self._wallet