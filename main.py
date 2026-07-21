from pathlib import Path
import json 
import random
import string

class Bank:
    database = "database.json"
    data = []

    try:
        if Path (database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"As error occured as {err} try again.")

    @classmethod
    def __update(cls):
        with open (cls.database,"w") as fs:
            json.dump(cls.data, fs, indent=4)

    def __generate_account_no(self):
        char = random.choices(string.ascii_uppercase, k=4)
        digits = random.choices(string.digits, k=8)
        acc_no = char + digits
        final = "".join(acc_no)
        return final

    def create_account(self):

        info = {
            "name" : input("Enter Your Name :- "),
            "age" : int(input("Enter Your Age :- ")),
            "mail" : input("Enter Your Mail :- "),
            "Balance" : 0,
            "account_no" : self.__generate_account_no(),
            "number" : int(input("Enter your 10 digit number :- "))

        }
        
        try:
             while True:
                pin = int(input("Enter your 4 digit pin :- "))
                if len(str(pin)) != 4:
                    print("Your pin must be of 4 digit try again :- ")
                else:
                    info["pin"] = pin
                    break
        except Exception as ValueError:
            print("You can only have numbers try again.")

        if info["age"] < 18:
            print("You are not eligible for creating account.")
            return
        else:
            Bank.data.append(info)
            Bank.__update()

    def deposite_money(self):
        acc_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))
        user = [i for i in Bank.data if i ["pin"] == pin and i["account_no"] == acc_no]

        if user:
            money = int(input("How much money you want to deposite :- "))
            if money > 100000 or money <= 0:
                print("You can not deposite more then 100000 rs or less than 0rs")
            else:    
                user[0]["Balance"] += money
                print("Money added successfully thanks visit again.")
                Bank.__update()
        else:
            print("Invalid Account Number or Pin.")

    def withdrawl_money(self):
        acc_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))
        user = [i for i in Bank.data if i ["pin"] == pin and i["account_no"] == acc_no]

        if user:
            money = int(input("How much money you want to withdrawl :- "))
            if money > user[0]["Balance"] or money <= 0:
                print("Insuficient Balance.")
            else:    
                user[0]["Balance"] -= money
                print("Money withdrawl successfully thanks visit again.")
                Bank.__update()
        else:
            print("Invalid Account Number or Pin.")

    def check_balance(self):
        acc_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))
        user = [i for i in Bank.data if i ["pin"] == pin and i["account_no"] == acc_no]
        if user:
            for i in user[0]:
                        print(f"Your balance is ₹{user[0]['Balance']}")
                        if i != "pin":
                            print(f"{i} : {user[0][i]}")
        else:
            print("Invalid Account Number or Pin.")


    def update_details(self):
        acc_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))
        user = [i for i in Bank.data if i ["pin"] == pin and i["account_no"] == acc_no]

        if user== False :
            print("Invalid number")
        else :
            newdata = {
                "name" : input("Enter to skip or type your new name :- "),
                "mail" : input("Enter to skip or type your new Mail :- "),
                "number" : input("Enter to skip or type your new number :- "),
                "pin" : input("Enter to skip or type your new pin :- ")
            }

            if newdata["name"] == "":
                newdata["name"] = user[0]["name"]
            if newdata["mail"] == "":
                newdata["mail"] = user[0]["mail"]
            if newdata["number"] == "":
                newdata["number"] = str(user[0]["number"])
            if newdata["pin"] == "":
                newdata["pin"] = user[0]["pin"] 

            newdata["pin"] = int(newdata["pin"])
            newdata["number"] = int(newdata["number"])

        for i in user[0]:
            if i in newdata:
                user[0][i] = newdata[i]
        print("Your details has been updated successfully.")
        Bank.__update()

    def deactivate_account(self):
        acc_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))
        user = [i for i in Bank.data if i ["pin"] == pin and i["account_no"] == acc_no]

        if user == False:
            print("Invalid number")
        else:
            print("Are you sure you want to deactivate your account? (yes/no)")
            check = input("Press Yes or No :- ")
            if check == "yes" or check == "Yes":
                index = Bank.data.index(user)
                Bank.data.pop(index)
                print("Your account has been deactivated successfully.")
                Bank.__update()
            else:
                print("OK")
                
    def exit(self):
        print("Thanks for using our services.")
        exit()

    
             
bank = Bank()


print("Press 1 for creating an Account")
print("Press 2 for Depositing Money")
print("Press 3 for Withdrawal Money")
print("Press 4 for Checking Balance")
print("Press 5 for Updating Details")
print("Press 6 for Deactivate Account")
print("Press 0 to Exit")

check = int(input("Tell your response :- "))

if check == 1:
    bank.create_account()

if check == 2:
    bank.deposite_money()

if check == 3:
    bank.withdrawl_money()

if check == 4:
    bank.check_balance()

if check == 5:
    bank.update_details()

if check == 6:
    bank.deactivate_account()

if check == 0:
    bank.exit()