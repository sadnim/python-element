from enum import Enum

class Account(Enum):
    KZT = "KZT"
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"

class BankAccount():
    id: int
    name: str
    surname: str
    account: Account
    value: float

    def __init__(self, id, name, surname, account) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.account = account
        self.balance = 0

    def addToBankAccount(self, value) -> None:
        self.balance += value
        print("Amount of money was successfully added to the account.")

    def substractFromBankAccount(self, value):
        if self.balance >= value:
            self.balance -= value
            print("Amount of money was successfully subtracted from the account.")
        else:
            print("Not enough balance! ")

    def moneyConversion(self, current_currency: Account, target_currency: Account, balance):
        cc = current_currency
        tc = target_currency
        if (cc == "RUB") :
            self.balance *= 7
        elif (cc == "USD"):
            self.balance *= 460
        elif (cc == "EUR"):
            self.balance *= 500
            
        if(tc == "RUB"):
            acc.account = Account.RUB
            self.balance /= 7
        elif(tc == "USD"):
            acc.account = Account.USD
            self.balance /= 460
        elif(tc == "EUR"):
            acc.account = Account.EUR
            self.balance /= 500


        print("Money conversion was successfully performed.")

    def toString(self):
        print("Bank Account ID: ", self.id)
        print("Owner's name: ", self.name)
        print("Owner's surname: ", self.surname)
        print("Current Balance: ", self.balance, self.account.value)

print("Hello! I am your bank assistant. Let's create your first account together!")
id = int(input("Type your ID: "))
name = input("Type your name: ")
surname = input("Type your surname: ")
currency = input("Choose currency (KZT, RUB, USD, EUR): ")
acc = BankAccount(id, name, surname, Account[currency])
print("Your account was successfully created!", "\n***********\n")

def menu():
    print("Now you can choose an action:")
    print("1. Print my account info")
    print("2. Deposit money to my account")
    print("3. Withdraw money from my account")
    print("4. Convert my balance to another currency")
    print("0. To exit and close program")
    
    action=input()

    if(action=="1"):
        print("**********")
        print(acc.toString())
        menu()
    elif(action=="2"):
        print("***********")
        print("What amount would you like to deposit?")
        amount=int(input())
        acc.addToBankAccount(amount)
        print("Your balance is now:", acc.balance, acc.account.value)
        menu()
    elif(action=="3"):
        print("***********")
        print("What amount would you like to withdraw?")
        amount=int(input())
        acc.substractFromBankAccount(amount)
        print("Your balance is now:", acc.balance, acc.account.value)
        menu()
    elif(action=="4"):
        print("***********")
        print("Your balance is:",acc.balance, acc.account.value, ". What currency would you like to convert to?(KZT, RUB, USD, EUR)")
        target_currency = input()
        acc.moneyConversion(acc.account.value, target_currency, acc.balance)
        print("Your balance is:", acc.balance, acc.account.value)
    elif(action=="0"):
        ...


menu()