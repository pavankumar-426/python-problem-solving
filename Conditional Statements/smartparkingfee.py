vehicle_type = int(input("Enter the vehicle type:\n"
                         "1. Bike\n"
                         "2. Car\n"
                         "3. SUV\n"
                         ": "))

parking_hours = int(input("Enter the parking hours: "))

day = input("Weekday/Weekend: ")

if parking_hours <= 0 or parking_hours > 24:
    print("Invalid Parking Hours")

elif vehicle_type == 1:
    if parking_hours <= 2:
        parking_amount = 20
    else:
        parking_amount = 20 + ((parking_hours - 2) * 10)

    if day == "Weekend":
        extra = parking_amount * 0.20
        final = parking_amount + extra
        print(final)
    else:
        print(parking_amount)

elif vehicle_type == 2:
    if parking_hours <= 2:
        parking_amount = 50
    else:
        parking_amount = 50 + ((parking_hours - 2) * 20)

    if day == "Weekend":
        extra = parking_amount * 0.20
        final = parking_amount + extra
        print(final)
    else:
        print(parking_amount)

elif vehicle_type == 3:
    if parking_hours <= 2:
        parking_amount = 80
    else:
        parking_amount = 80 + ((parking_hours - 2) * 30)

    if day == "Weekend":
        extra = parking_amount * 0.20
        final = parking_amount + extra
        print(final)
    else:
        print(parking_amount)

else:
    print("Invalid Vehicle Type")