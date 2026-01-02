from abc import ABC, abstractmethod


class LoggeerMixin:
    def log_trasaction(self,amount, status):
        print(f"[LOG] Trasaction of {amount}- Status: {status}")

    
class Payment(ABC):


    @abstractmethod
    def process_payment(self,amount):
        pass


class CreditCard(Payment,LoggeerMixin):
    def process_payment(self, amount):
        print("process credit card payment---")
        self.log_trasaction(amount,"SUCCESS")


class PayPal(Payment,LoggeerMixin):
    def process_payment(self, amount):
        print("process credit card payment---")
        self.log_trasaction(amount,"SUCCESS")



def make_payment(payment_method,amount):
    payment_method.process_payment(amount)


credit_cards = CreditCard()
paypal = PayPal()

make_payment(credit_cards,1000)
make_payment(paypal,5000)