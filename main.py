import user #register or login
import transaction #add, view, update and delete transaction
import report #for the report
import budget #set and check the budget

# main page 
def main():
    print("*"*50)
    print("Welcome to Personal Finance Management Application")
    print()
    print("Press 1 for Login")
    print("Press 2 for New Registration")
    print("Press 0 to Exit")
    print("*"*50)
    choice_main()

# after loging page
def main2(id):
    print("*"*50)
    print("Welcome to Personal Finance Management Application")
    print()
    print("Press 1 for Add transaction")
    print("Press 2 for View transactions")
    print("Press 3 for Delete transaction")
    print("Press 4 for Update transaction")
    print("Press 5 for All report")
    print("Press 6 for Set budget")
    print("Press 7 for Check budget")
    print("Press 0 for Logout ")
    print("*"*50)
    choice_main2(id)


# related to login page (main function)
def choice_main():
    choice = int(input("Enter the key: "))
    if(choice == 1):
        id = user.login()
        main2(id)
    elif(choice == 2):
        user.register()
    elif(choice == 0):
        exit()
    else:
        print("...press valid value...")
        choice_main()

# related to after loging page (main2 function)
def choice_main2(id):
    choice2 = int(input("Enter the key: "))
    if(choice2 == 1):
        amount = int(input("Enter the Amount: "))
        des = input("Enter the Category (Food, Rent, Salary): ")
        type = input("Enter Type of Transaction (income or expense): ")
        transaction.add_transaction(id, amount, des, type)
    elif(choice2 == 2):
        transaction.view_transactions(id)
    elif(choice2 == 3):
        t_id = int(input("Enter the Transaction Id: "))
        transaction.delete_transaction(t_id)
    elif(choice2 == 4):
        t_id = int(input("Enter the Transaction Id: "))
        amount = int(input("Enter the Amount: "))
        des = input("Enter the Category (Food, Rent, Salary): ")
        type = input("Enter Type of Transaction (income or expense): ")
        transaction.update_transaction(t_id, amount, des, type)
    elif(choice2 == 5):
        print("Press 1 for Monthly report")
        print("Press 2 for Yearly report")
        num = int(input())
        report.generate_report(id, num)
    elif(choice2 == 6):
        des = input("Enter the Category (Food, Rent, Salary): ")
        amount = int(input("Enter the Amount: "))
        budget.set_budget(id, des, amount)
    elif(choice2 == 7):
        budget.check_budget(id)
    elif(choice2 == 0):
        print("Logout Successfully...")
        main()
    else:
        print("...press valid value...")
        choice_main()


# execute the code from here
if __name__ == "__main__":
    main()