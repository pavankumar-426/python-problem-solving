withdraw=int(input("Enter the withdrawl amount: "))
balance=1000
if withdraw<=0:
    print("Invalid Amount")
elif withdraw>balance:
    print("Insufficent Balance")
elif withdraw%100!=0:
    print("Enter the Multiples of 100")
else:
    print("Withdrawl Sucessful")