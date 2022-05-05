# Banking app


import json
from tkinter.messagebox import YES
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db_customers = client.bankapp
db_customers = db_customers.customers

#reading JSON file
def readJson():
    with open('customer.json') as f:
        customers = json.load(f)
        
        f.close()
        return customers
        
def addToMongo():
    customers = readJson()
    print(customers)
    for user in customers['customers']:
        print(user)
        db_customers.insert_one(user)
       
#addToMongo()
#banking application

#Creating a new user
def createAccounts():
    custName =input("Enter customer first and last name\n")
    password =int(input("create password\n"))
    mobile = input("Enter Mobile number\n")
    bal=int(input("Enter initial balance\n"))
    accountNo=int(input("Enter account number\n"))

    new_user={
        "customer name": custName,
        "account number": accountNo,
        "phone": mobile,
        "balance": bal,
        "password": password,
        
    }
    db_customers.insert_one(new_user)

# def showAcctDetails():
#     print("AccountNo:", accountNo)
#     print("CustomerName:", custName)
#     #print(pin:" ,pin)
#     print("Mobile:", mobile)

def deposit(phone,amount):
    user=db_customers.find_one({"phone":phone})
    print(user)
    user["balance"]=user["balance"]+amount
    db_customers.update_one({"phone":phone},{"$set":{"balance":user["balance"]}})
    print(user)
    print("Your balance is ",user["balance"])


    #checkBalance()
def withdraw(phone,amount):
    user=db_customers.find_one({"phone":phone})
    print("Your balance is ",user["balance"])
    if amount>user["balance"]:
        print("insufficient funds")
        print("Your balance is ",user["balance"])
    else:
        user["balance"]=user["balance"]-amount
        db_customers.update_one({"phone":phone},{"$set":{"balance":user["balance"]}})
    print("Your balance is ",user["balance"])

def checkBalance(phone):
    user=db_customers.find_one({"phone":phone})
    print("Your balance is ",user["balance"])

def deleteAccount(phone):
    db_customers.delete_one({"phone":phone})


    #__main__#
def main():
    print("Hello, Welcome to ABC Bank")
    while True:
        print("please choose yes, no, or quit" )
        
        option= input("Are you an existing customer" )
        if option== "yes":
            mobile= input("Please enter your phone #" )
            password=input("Please enter your password" )
            
            if not db_customers.find_one({"phone":mobile}):
                print("mobile is not correct")
            else:

                       

                while True:

                    print(" 2. Withdraw \n 3. Deposit \n 4. Check Balance \n 5.Delete account\n 6.Goodbye")  
                    ch = int(input("Please make a selection from the main menu"))
                

                    if (ch==2):
                        print("Let's make a withdrawal")
                        amnt =int(input("Enter amount to Withdraw"))
                        withdraw(mobile,amnt)
                    
                    elif (ch==3):
                        print("Let's make a deposit")
                        amnt=int(input("Enter amount to deposit"))
                        deposit(mobile,amnt)
                    

                        
                    elif (ch==4):
                        print("check balance")
                        checkBalance(mobile)
                    elif (ch==5):
                        print(" Thank you for banking with ABC, Goodbye")
                        deleteAccount(mobile)

                    elif(ch==6):
                        print("Goodbye")
                        break
                    else:
                        print("please select any of the  5 options above")
        
        elif option=="no":
            print("Let's create account ")
            createAccounts()
        elif option=="quit":
            break
        else:
            print("please choose yes, no, or quit")            
main()
