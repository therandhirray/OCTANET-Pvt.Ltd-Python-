import time

print("Please Insert Your Card")
time.sleep(5)

balance = 2000
password = 1234
pin=int(input("Enter your pin "))

if pin==password:
    while True:
        print("******************************************")
        print("******************************************")
        print("1) Check Balance \t 2) Deposite \n3) Withdraw      \t 4) Exit")
        
        try:
            option = int(input("Enter your Choice: "))
        except:
            print("Enter valid Option ")
        
        if option == 1:
            print(f"Your Current Balance is {balance}")
        
        if option == 2:
            deposite_amount = int(input("Enter Deposite Amount:"))
            balance = balance+deposite_amount
            print(f"{deposite_amount} amount is Credited to your Account")
            print(f"Your Current Balance is {balance}")
        
        if option == 3:
            withdraw_amount = int(input("Enter Withdrawal Amount:"))
            balance = balance-withdraw_amount
            print(f"{withdraw_amount} amount is Debited from your Account")
            print(f"Your Current Balance is {balance}")
            
        if option == 4:
            break
else:
    print("Wrong Pin ! Please try again ")