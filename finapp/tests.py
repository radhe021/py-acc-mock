from django.test import TestCase

# Create your tests here.
# Create a new account
account = AccountUseCase.create_account(1, 'John Doe', 'johndoe@example.com', '1234567890')

# Make a deposit
TransactionUseCase.make_transaction(account.account_id, 1000, 'deposit')

# Make a withdrawal
TransactionUseCase.make_transaction(account.account_id, 500, 'withdraw')

# Generate account statement
print(StatementUseCase.generate_account_statement(account.account_id))

# Delete the account
account.delete()

# Delete the customer
customer = Customer.objects.get(pk=1)
customer.delete()
