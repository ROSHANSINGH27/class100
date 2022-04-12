from unittest import result


class atm():
    pin=12345678
    cardNumber=23456789
    cash=0
    balanceenquiry="not possible"
    cash1="withdrawl"
    cash2="balanceenquiry"
    pin1=input("enter your pin\n")
    cardNumber1=input("enter your card number\n")
    if(pin1==pin):
     print("your pin was correct")
     if(cardNumber==cardNumber1):roshan=input("what do you want to do either withdrawl or balance enquiry\n")
     if(roshan==cash1):print(cash)
     if(roshan==cash2):
         print(balanceenquiry)

    if(pin1!=pin):
        print("your pin was wrong")
    if(cardNumber1!=cardNumber):
        print("your cardnumber was wrong")
     

