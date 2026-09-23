from abc import ABC,abstractmethod
class BankApp(ABC):

    def database(self):
        print('Connected to database')

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):

    def nobile_login(self):
        print('login into mobile')

    def security(self):
        print('Mobile securoty')

mob = MobileApp()
