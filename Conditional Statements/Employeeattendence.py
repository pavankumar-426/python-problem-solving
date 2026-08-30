a=int(input("Enter the attendance_percentage:"))
r=int(input("Enter the performance_rating:"))
if a>=95 and r>=4:
    print("20% Bonus")
elif a>=90 and r>=4:
    print("15% Bonus")
elif a>=85 and r>=3:
    print("10% Bonus")
else:
    print("No bonus")