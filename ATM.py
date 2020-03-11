import sys
#Hunter Holcombe
#Final Project Milestone Three

#account balance 
account_balance = float(500.25)


#printbalance function takes the current balance and prints it for the user
def print_balance():
    return account_balance

    
#deposit function takes input for the deposit amount
#it then calculates the current balance and returns this along with the deposit amount
def deposit(account_balance):
    account_balance = print_balance() + float(deposit_amount)
    return account_balance

  
#withdraw function takes input for the withdrawal amount
#it then determines if there is enough in the account balance in order
#to withdraw, if it doesn't the return lets the user know
#if there is enough then it calculates the current balance and returns it
#along with the withdrawal amount
def withdraw(account_balance):
    account_balance = print_balance() - float(withdrawal_amount)
    return account_balance


userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
    deposit_amount = input ("How much would you like to deposit today?\n")
    print(deposit (account_balance))
    print("Deposit amount was $" + str(format(float(deposit_amount), '.2f')) + ", current balance is $" + str(deposit(account_balance)))
elif(userchoice == 'B'):
    print("Your current balance: " + str(print_balance()))
elif(userchoice == 'W'):
  withdrawal_amount = input ("How much would you like to withdraw today?\n")
  if float(withdrawal_amount) > print_balance():
    print("$" + str(format(float(withdrawal_amount), '.2f')) + " is greater than your account balance of $" + str(account_balance))
  elif float(withdrawal_amount) <= account_balance:
    print("Withdrawal amount was $" + str(format(float(withdrawal_amount), '.2f')) + ", current balance is $" + str(withdraw(account_balance)))
elif(userchoice == 'Q'):
    print("Thank you for banking with us.")
