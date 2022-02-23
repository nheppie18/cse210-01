from balloon import Balloon
from airtank import Airtank
from wallet import Wallet
from person import Person

class Clown(Person):
    def __init__(self):
        self.__tank = Airtank("Helium")

    def buy_balloon(self, cost) -> Balloon:
        balloon = Balloon("Red")
        balloon.fill(self.__tank.release_air(500))
        self._wallet.add_transaction(cost)
        return balloon

    def __str__(self):
        return f"Clown (${super()._wallet.get_balance():.2f})"