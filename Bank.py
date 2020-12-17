import math

class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __str__(self):
        return 'Customer [{0}, {1}, {2}, {3}]'.format(self.customer_id, self.first_name, self.last_name, self.email )


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self._balance = 1000
        Account.last_id += 1
        self.customer_id = Account.last_id
        self.interest_rate = 0.01
        self.years = 0
        self.interest = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Added: " + str(amount) + ", the new balance is: " + str(self._balance))
        else:
            print("You can only deposit a positive amount")

    def charge(self, amount):
        self._balance -= amount
        if self._balance >= amount:
            self._balance -= amount
            print("Charged: " + str(amount) + ", the new balance is: " + str(self._balance))
        else:
            print("You do not have enough money on your account to withdraw: " + amount)

    def get_balance(self):
        return self._balance


    def calc_interest(self):
        self.years = 10
        if self._balance > 0:
            self.interest = math( self._balance * self.interest_rate * self.years ) / 1000
            print( "Your interest is" + str(self.interest) )
        else:
            self.interest = 0
            print( "Your interest is 0" )

    def __str__(self):
     return 'Account [{0}, {1}, {2}, {3}, {4}]'.format(Account.last_id, self.customer, self._balance, self.interest_rate, self.interest)

class Bank:
    def __init__(self):
        self._accounts = []
        self._customers = []

    def create_customer(self, first_name, last_name, email):
        c = Customer( first_name, last_name, email )
        self._customers.append( c )
        return c

    def create_account(self, customer):
        a = Account( customer )
        self._accounts.append( a )
        return a

    def transfer(self, acc_from, acc_to, amount):
        # TODO - implement it (1st thing to do - input parameters are account ids)
        pass

    def __str__(self):
        return 'Bank[{0},{1}]'.format( str( self._customers ), str( self._accounts ) )


bank = Bank()

c = bank.create_customer( 'Kasia', 'Szeremeta', 'szeremeta.kasia@gmail.com' )
print( c )

a = bank.create_account( c )
a.deposit( 1.00 )
print( a )

c2 = bank.create_customer( 'Ktoto', 'Hallo', 'k.toto@gmail.com' )
print( c2 )

a2 = bank.create_account( c2 )
a2.deposit( 5000000 )
print( a2 )

print( bank )

# c = Customer('Kasia', 'Szeremeta', 'szeremeta.kasia@gmail.com')
# print(c)

# a = Account(c)
# a.deposit (100000.00)
# print(a)