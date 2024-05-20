from bank_account import *

Pankaj = BankAccount(1000, "Pankaj")
Athrav = BankAccount(2000, "atharv")

Pankaj.get_balance()
Athrav.get_balance()

Athrav.deposit(500)

Athrav.withdraw(10000)
Pankaj.withdraw(10)

Pankaj.transfer(10000, Athrav)
Pankaj.transfer(100, Athrav)

Abhi = InterestRewardsAcct(1000, "Abhi")

Abhi.get_balance()

Abhi.deposit(100)

Abhi.transfer(100, Pankaj)

Madhuresh = SavingsAcct(1000, "Madhresh")

Madhuresh.get_balance()

Madhuresh.deposit(100)

Madhuresh.transfer(10000, Athrav)
Madhuresh.transfer(1000, Athrav)