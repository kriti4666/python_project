class MoneyMachine:
    """models the payment of the drink"""
    CURRENCY = "$"
    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """print the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coin(self):
        """returns the total calculated from coins money received"""
        print("Please insert coins.")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How much {coin} "))
        return self.money_received

    def make_payment(self, cost):
        """returns True when payment is accepted, False if payment not done"""
        self.process_coin()
        if self.money_received >= cost:
            change = self.money_received - cost
            print(f"Here is {self.CURRENCY} {change} your change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money.Money refunded.")
            self.money_received = 0
            return False


