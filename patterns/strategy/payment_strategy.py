"""This module defines the PaymentStrategy class."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PaymentStrategy(ABC):
    """"""

    @abstractmethod
    def process_payment(account: BillingAccount, payee: Payee, amount: float) -> str:
        """
        """
        pass