

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withwdraw(self,amount):
        if amount<0:
            raise Exception('amount cannot be -ve')
        if self.balance<amount:
            raise Exception('not enough money')
        self.balance = self.balance - amount

obj = Bank(100000)
try:
    obj.withwdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)


# Custom Exception
class MyException(Exception):
    def __init__(self,message):
        print(message)

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withwdraw(self,amount):
        if amount<0:
            raise MyException('amount cannot be -ve')
        if self.balance<amount:
            raise MyException('not enough money')
        self.balance = self.balance - amount

obj = Bank(100000)
try:
    obj.withwdraw(5000)
except MyException as e:
    pass
else:
    print(obj.balance)

