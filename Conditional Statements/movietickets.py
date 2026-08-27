age=int(input("Enter the Age : "))
ticket=int(input("Enter your Ticket price : "))
if age<5:
    print("Free Ticket")
elif 5<=age<=17:
    print("Child Ticket")
    ticketd=ticket*0.5
    ticketp=ticket-ticketd
    print(f"You Clamied 50% Disccount Your Ticket price\n={ticketp}")
elif 18<=age<=59:
    print("Adult Ticket ")
    print(f"You Have No Discount")
elif age>60:
    print("Senior Citizen")
    ticketd=ticket*0.3
    ticketp=ticket-ticketd
    print(f"You Clamied 30% Disccount Your Ticket price \n={ticketp}")