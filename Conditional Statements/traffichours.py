hours=int(input())
member=int(input())
if hours>0:
    if hours<=2:
        fee=50
        print(fee)
    elif 2<=hours<=5:
        fee=100
        print(fee)
    elif 5<=hours<=10 and member==1:
        fee=150
        dis=fee*0.2
        final=int(fee-dis)
        print(final)
    elif hours>=10 and member==1:
        fee=200
        dis=fee*0.2
        final=int(fee-dis)
        print(final)
else:
    print("Invalid hour")