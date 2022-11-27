balance=0

def addToBankAccount(value):
    global balance
    balance+=value
def substractFromBankAccount(value):
    global balance
    balance-=value
def moneyConversion(value, initial, to):
    if(initial=="USD" and to=="KZT"):#dollars into tenge
        print(value*470)
    elif(initial=="KZT" and to=="USD"):#tenge into dolars
        print(value/470)

addToBankAccount(500)
print(balance)
substractFromBankAccount(300)
print(balance)
moneyConversion(200, "USD", "KZT")