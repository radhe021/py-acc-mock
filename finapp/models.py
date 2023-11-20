from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class AccountUseCase:
    @staticmethod
    def create_account(customer_id, name, email, phone_number):
        customer = Customer.objects.create(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        account = Account.objects.create(customer_id=customer.customer_id, account_number=str(customer.customer_id) + '001', balance=0)
        return account

class TransactionUseCase:
    @staticmethod
    def make_transaction(account_id, amount, transaction_type):
        account = Account.objects.get(pk=account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)

class StatementUseCase:
    @staticmethod
    def generate_account_statement(account_id):
        account = Account.objects.get(pk=account_id)
        return f"Account ID: {account.account_id}, Balance: {account.balance}"

class AccountRepository:
    @staticmethod
    def save_account(account):
        account.save()

    @staticmethod
    def find_account_by_id(account_id):
        return Account.objects.get(pk=account_id)

    @staticmethod
    def find_accounts_by_customer_id(customer_id):
        return Account.objects.filter(customer_id=customer_id)
