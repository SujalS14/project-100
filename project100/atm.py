class Atm(object):
    """
    Welcome to the Bank ATM
    """

    def __init__(self, cardNumber, pinNumber, amountWithdrawl, balanceEnquiry):
        self.cardNumber= input("Enter Card Number:-")
        self.pinNumber= input("Please Enter Pin Number:-")
        self.amountWithdrawl=input("How much money:-")
        self.balanceEnquiry=input("Whats the amount:-")

    def cardNum(self):
        print("002")

    def pinNum(self):
        print("124")

    def withdraw(self):
        print("201")

    def remaining(self):
        print("11")
    

    bobby = Atm("001", 123, 200, 10)

    print(bobby.start())
    print(bobby.amountWithdrawl)