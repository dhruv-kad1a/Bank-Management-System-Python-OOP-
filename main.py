import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such File Exist")
    except Exception as err:
        print(f"an exception occurecd as {err}")

    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha  =random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    


    def createaccount(self):
        info = {
            "name": input("Yell Your Name :- "),
            "age": int(input("Tell Your Age :- ")),
            "email" : input("Tell Your Email :- "),
            "pin": int(input("Tell Your 4 number Pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance":- 0  
        }
        if info['age'] < 18 or  len(str(info["pin"])) != 4:
            print("Sorry you cannot Create your Account")
        else:
            print("account has been Create Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note-down your Account Number")

            Bank.data.append(info)
            Bank.__update()

    def depositemoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("how much you want to Deposite :- "))
            if amount > 10000 and amount < 0:
                print("Soory the amount is too much you can deposite below 10k and above 0")
            else :
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount Deposited Successfully")


    def withdrawmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("how much you want to Withdraw :- "))
            if userdata[0]['balance'] < amount:
               print("Sorry u dont have that much money to withdrawe")
            else :
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew Successfully")

    def showdetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        print("Your Information are :- \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found")
        else:
            print("you cannot change Age, AccNo.,Balance")

            print("Fill Details for Change or Leave it empty if no chnage")

            newdata = {
                "name":input("Please tell new name or press enter :- "),
                "email":input("Please tell new email or press enter :- "),
                "pin":input("enter new pin or press enter to skip :- ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def deletacc(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("no such data exist")
        else:
            check = input("Press Y if you actually want to delete the Acc or Press Enter :- ")
            if check == 'y' or check == 'Y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("successfully deleted")
            else:
                print("bypassed")



user = Bank()
print("Press 1 for Creating an Account")
print("Press 2 for Depositing Money in the Bank")
print("Press 3 for Withdrawing the Money")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Deleting Your Account")

check = int(input("tell your Response :- "))

if check ==  1 :
    user.createaccount()

if check == 2:
    user.depositemoney()

if check == 3:
    user.withdrawmoney()

if check == 4 :
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deletacc()