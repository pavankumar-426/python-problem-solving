data=int(input("Enter the Data Used : "))
pl=int(input("Enter the plan limit "))
if data<=80:
    print("Normal Usage ")
elif 80<= data <=100:
    print("Data Almost Finished ")
elif data >=100:
    print("Extra Data Charges ")
elif data >=5000:
    print("Heavy Overuse")