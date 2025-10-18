"""This module defines the PartialPaymentStrategy class."""

__author__ = "Ridham Sood "
__version__ = "1.0.0"

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PartialPaymentStrategy(PaymentStrategy):
    """"""

    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """
        """

        account.deduct_balance(payee, amount)
        updated_balance = account.get_balance(payee)

        if updated_balance <= 0:
            return f"Processed payment of ${amount:.2f}. New Balance: ${updated_balance:.2f}"
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${updated_balance:.2f}."

