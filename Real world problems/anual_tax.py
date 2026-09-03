income=int(input())
if income<0:
    print("Please Enter Positive values")

elif income<=150000:
    tax=0
    print(f"Tax = {tax}")
elif 150000<=income<=300000:
    tax=(income-150000)*0.10
    print(f"Tax = {tax}")
elif 300000<=income<=500000:
    tax=(income-300000)*0.20
    print(f"Tax = {tax}")
elif income>=500000:
     tax=(income-500000)*0.30
     print(f"Tax = {tax}")

