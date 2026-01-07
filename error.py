# name = input("enter your name:")


# class InvalidMarksError(Exception):
#     pass 

# try :
#     maths = int(input("enter maths marks:"))
#     phy = int(input("enter physics marks:"))
#     eng = int(input("enter english marks:"))

#     marks = [maths , phy , eng]

#     for i in marks:
#         if i<0 or i>100:
#             raise InvalidMarksError("marks must be between 0 to 100")
    
#     avg_marks  = sum(marks)/len(marks)

#     print(f"{name} your average score is :" , avg_marks)

# except ValueError:
#     print("error : please enter valid integers")

# except InvalidMarksError as e:
#     print("custom error:" , e)

# else :
#     if (avg_marks>75):
#         print("you scored really well")
#     elif(avg_marks<75 and avg_marks > 35):
#         print("you need to work hard")
#     else:
#         print("you failed!")

# finally:
#     print("program execution is done.")

Accountholder_name = input("enter your name :")


class NegativeAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

def NegativeAmount(amount):
    if(amount<0):
        raise NegativeAmountError("please enter valid amount.")

def InsufficientBalance(w_amt , total_bal):
    if (w_amt > total_bal):
        raise InsufficientBalanceError("your balance is insufficient.")

try :

    Intial_balance = float(input("enter your intial balance:"))
    NegativeAmount(Intial_balance)
    total_bal = Intial_balance 

    while True:
        print("1.Deposit money",end=" ")
        print("2. withdraw money", end =" ")
        print("3.check balance")
        print("4.exit")


        choice = int(input("enter your choice:"))

        if (choice == 1):
           d_amt = float(input("enter the amount you want to deposit:"))
           NegativeAmount(d_amt)

           print(f"{Accountholder_name} you deposit Rs.{d_amt} .")
           total_bal = total_bal + d_amt
           

        elif(choice == 2):
            w_amt = float(input("enter the amount you want to withdraw:"))
            NegativeAmount(w_amt)
            InsufficientBalance(w_amt,total_bal)

            print(f"{Accountholder_name} you withdrew Rs.{w_amt}.")
            total_bal = total_bal - w_amt
            
       
        elif(choice == 3):
            print(f"{Accountholder_name} your total balance is {total_bal}")

        elif(choice == 4):
            print("Thank you for connecting with us.")
            break
    
        else:
          print("please enter a valid choice.")

except NegativeAmountError as e:
    print(e)

except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("enter valid Integers.")

