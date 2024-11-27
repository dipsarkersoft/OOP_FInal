class Bank():
    is_bankrupt=False
    is_loan=False

    def __init__(self,name,bankamn):
        self.name=name
        self.total_balance=bankamn
        self.total_loan=0
        self.users=[]
        self.admin=[]

    def add_user(self,user):
        user.id=len(self.users)+1
        self.users.append(user)
        return user

    def all_user(self):
        print("----------------------------")
        print("ID\tName\tEmail\tAdress\tAccount_type\tLoanTime\tBalance")
        for user in self.users:       
            print(f"{user.id}\t{user.name}\t{user.email}\t{user.adress}\t{user.account_type}\t{user.loantime}\t{user.balance}")
 
    def deposit_bal(self,id,ammount):
        print("----------------------------")
        if ammount >0:
            for user in self.users:
                if user.id == id:
                    user.balance+=ammount
                    self.total_balance+=ammount
                    user.trans_his.append(TransHistory("deposit",ammount))
                    print("Deposit Succes")
                    return
                else:
                    print("No User Found")      
        else:
            print("Not Possible ")    


    def delete_user(self,id):

        print("----------------------------")
        for usr in self.users:
            if usr.id==id:
                self.users.remove(usr)
                print(f"User {id} delete Sucess")
                return
        print("No user Found")


class TransHistory:
    def __init__(self,trans_type,ammount):
        self.trans_type=trans_type
        self.ammonut=ammount

                        


class User:
    def __init__(self,name,email,adress,account_type):
        self.id=None
        self.name=name
        self.email=email
        self.adress=adress
        self.account_type=account_type
        self.trans_his=[]
        self.loantime=0
        self.my_to_loan=0
        self.balance=0
    
    def with_drawbal(self,bank,amm):
        print("----------------------------")
        if bank.is_bankrupt:
            print("The Bank Is Bankrupt")
        else:
            if self.balance > amm and amm > 0:
                self.balance-=amm
                self.trans_his.append(TransHistory("Withdraw",amm))
                print(f"{amm} Withdraw Sucess")
            else:
                print("Withdrawal amount exceeded")    


    def cheak_bal(self):
        print("----------------------------")
        print(f"Your Available Balance { self.balance} TK")

    def Chea_transhis(self):
        print("----------------------------")
        print("Trans Type \t Ammonut")
        print("----------------------------")
        for trans in self.trans_his:
            print(f"{trans.trans_type}\t\t{trans.ammonut}")
   

    def take_loan(self,bank,ammount):
        print("----------------------------")
        if bank.is_loan:
            print("Loan feature Off")
        else:
            if bank.total_balance>ammount:
                if self.loantime <2:
                    self.my_to_loan+=ammount
                    self.balance+=ammount
                    bank.total_balance-=ammount
                    bank.total_loan+=ammount
                    self.loantime+=1
                    self.trans_his.append(TransHistory("Loan",ammount))
                    print(f"Loan Sucess {ammount}")
                else:
                    print("You cannot take the loan more than 2 times"
                    )    

            else:
                print(f"{ammount} is Not Possible")

    def my_total_loan(self):
        print("----------------------------")
        print(self.my_to_loan)

    def transfer_money(self,bank,id,ammount):
        print("----------------------------")
        if self.balance >ammount:
            for user in bank.users:
                if user.id == id:
                    user.balance+=ammount
                    self.balance-=ammount
                    user.trans_his.append(TransHistory(f"Sender Id {self.id}",ammount))
                    self.trans_his.append(TransHistory(f"Send Id {id}",ammount))
                    print(f"User ID {id} . {ammount} Send Sucess ")
                    return

            else:
                print(f"Account does not exist")
                
        else:
            print("Not Enough Money")     
           


class Admin:
    def __init__(self,bank):
        self.user="admin"
        self.pas="123"
        self.bank=bank

    def delete_account(self,id):
        self.bank.delete_user(id)

    def all_user(self):
        self.bank.all_user()

    def bank_total_bal(self):
        print(self.bank.total_balance)
    
    def toal_loan_ammount(self):
        print(self.bank.total_loan)          

        
    def loan_off(self):
        self.bank.is_loan =True
        print("Loan Off Sucess")
    def loan_on(self):
        self.bank.is_loan =False
        print("Loan On Sucess")    
   
    def isbankruft(self):
        self.bank.is_bankrupt =True
        print("Our Bank is Bankrupt ")






bn=Bank("Mm",100000000)



def login_user(bank,id):
    for user in bank.users:
        if user.id == id:
            return user
        else: 
            print("No User Found")        


def User_func(usr):
    #print(usrpass.name)
    
    print("----------------------------")
    while True:
        print("----------------------------")
        print(f"ID : {usr.id} Name : {usr.name} ")
        print("----------------------------")
        print("1.Deposit Your Account: ")
        print("2.Withdraw Ammount: ")
        print("3.Available Balance: ")
        print("4.Transaction History: ")
        print("5 . Send Money ")
        print("6 .Loan ammount ")
        print("7 .Exit ")
        x=int(input("Enter Your Choice: "))

        if x==1:
            id=int(input("Enter Your Account id: "))
            ammount=int(input("Enter Your Deposit ammount: "))
            bn.deposit_bal(id,ammount)

        elif x==2:
            ammount=int(input("Enter WithDraw ammount: "))
            usr.with_drawbal(bn,ammount)
            
        elif x==3:
            usr.cheak_bal()
        elif x==4:
            usr.Chea_transhis()
        elif x==5:
            id=int(input("Enter Reciver ID: "))
            ammount=int(input("Enter  ammount: "))
            usr.transfer_money(bn,id,ammount)
        elif x==6:
            loan_ammount=int(input("Enter Loan Ammount: "))

            usr.take_loan(bn,loan_ammount)
        elif x==7:
            break
        else:
            print("Invalid Index")
                

    

def Admin_func(admn):
    


    while True:
        print("----------------------------")
        print("1.Delete User : ")
        print("2.See all user : ")
        print("3.Total Available Balance Of The Bank: ")
        print("4. Total Loan Amount.: ")
        print("5. On Loan Feature  ")
        print("6. Of Loan Feature ")
        print("7.Set Bankruft:  ")
        print("8.Exit ")
        x=int(input("Enter Your Choice: "))

        if x==1:
            id=int(input("Enter  Account id : "))
            admn.delete_account(id)

        elif x==2:
            admn.all_user()
            
        elif x==3:
            admn.bank_total_bal()
        elif x==4:
            admn.toal_loan_ammount()
        elif x==5:
            admn.loan_on()
        elif x==6:
            admn.loan_off()
            
        elif x==7:
            admn.isbankruft()
        elif x==8:
            break    
        else:
            print("Invalid Index")
    
    


while True:
    print("----------------------------")
    print("1. Register Or login as a User: ")
    print("2. Login As a Admin: ")
    print("3. Break: ")
    x=int(input("Enter Your Input: "))
    
    if x==1:
        
        x=input("Login(l) / Register (r)")
        if x=='l':
            id=int(input("Enter Your Id"))
            lngusr=login_user(bn,id)
            print(f"Welcom {lngusr.name} ")
            User_func(lngusr)

        elif x=='r':
            name=input("Enter Your Name : ")    
            email=input("Enter Your Gmail : ")    
            location=input("Enter Your Location : ")    
            account_type=input("Enter Account Type (Savings/Cuurent) :")
            ruser=User(name,email,location,account_type)
            bn.add_user(ruser)
            User_func(ruser)
            #print(f"Welcom {ruser.name} ")
        else:
            print("Invalid Index")

             
    elif x==2:
        user=input("Enter Your UserName: ")
        passw=input("Enter Your PassWord: ")
        if user=="admin" and passw=="123":
            admn=Admin(bn)
            Admin_func(admn)

        else:
            print("Wrong Password")    

    elif x==3:
        break
    else:
        print("Invalid Input")        


