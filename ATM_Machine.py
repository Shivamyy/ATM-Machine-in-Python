from prettytable import PrettyTable

user_details={
    "user_id" : "shivam",
    "user_pin" : 1234,
}
INITIAL_BALANCE=100000
class Atm:
    def accept_details(self,balance_left):
        self.balance_left=balance_left
        print("Insert your card.")
        user_id=input("Enter your id please: ")
        user_pin=int(input("Enter your pin: "))
        if user_id==user_details["user_id"] and user_pin==user_details["user_pin"]: 
            print("Withdrawable Amounts")
            amounts=PrettyTable()
            amounts.add_column("Column_2",["5000","10000","15000","20000"])
            amounts.add_column("Column_1",["1000","2000","3000","4000"])
            print(amounts)
            withdraw_amount=int(input("Please select one of the amounts from above: "))

            if withdraw_amount<20000 and withdraw_amount<INITIAL_BALANCE:
                print("Processing....")
                print("Please, take your card.")
                print(f"Collect your {withdraw_amount} money.")
                print("Thank You! Visit Again.")
                balance_left=INITIAL_BALANCE-withdraw_amount 
            
            else:
                print("You can withdraw 20000 only per day and better to select the amount from the above list.")
        else:
             print("❌❌Id and pin does not match❌❌\nEnter the correct id and pin.")
        
        # print(f"Balance left in the ATM {balance_left}")   # yo user lai dekhauna pardaina
    def recharge_atm(self):
        if self.balance_left==0:
            new_balance_in_atm=INITIAL_BALANCE
            print(new_balance_in_atm)

shivam=Atm()

shivam.accept_details(balance_left=INITIAL_BALANCE)
shivam.recharge_atm()