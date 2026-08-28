amount=int(input("Enter The Order  Amount ; "))
dd=int(input("Enter The delivary Distance: "))
pm=int(input("Select Your ayment Option : \n " \
"\n1.UPI" \
"\n2.Card" \
"\n3.CaSh On Delivery \n"  ))
if amount<500:
    print("Minimum Order is not  reched !")
elif dd>20:
    print("Delivery is not avalible ")
elif pm==3:
    if amount<=5000:
        print("Cash on Delivery Acepted ")
    else:
        print("Cash on Delivery Not  Acepted ")
elif pm==2 or pm==3:
    print("Order Accepted")

