from abc import ABC, abstractmethod
import functools

from sympy.physics.units import amount


#Level 2 (PaymentSystem)


#Decorator 1 login
def log_payment(func):
    @functools.wraps(func)
    def wrapper(self, amount, *args, **kwargs):
        print(f"[LOG] Intention of payment: {amount} RON")
        result = func(func, amount, *args, **kwargs)
        print(f"[LOG] Payment invoice: {result}RON")
        return result
    return wrapper

#Abstract interface
class CreditCardProcessor(PaymentProcessor):
    @log_payment
    def pay(self, amount: float): -> None :
        print(f"Payment with debit card: {amount} RON processed")

class PayPalProcessor(PaymentProcessor):
    @log_payment
    def pay(self, amount, float): -> None :
        print(f"Payment with PayPal: {amount} RON processed")

#Polimorfism
def run_processor(payment: list[PaymentProcessor], amount: float):
    for p in pay:
        p.pay(amount)

#EXECUTE
if __name__ == "__main__":
processor = [CreditCardProcessor(), PayPalProcessor()]
run_payments(processor, 150.0)

