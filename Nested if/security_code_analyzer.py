n=int(input("Enter the Three Digits Number"))
f=n//100
s=(n//10)%10
t=n%10
if 100 <= n <= 999:
    if f==s or f==t or s==t:
        print("Repeated number")
    if f<s<t:
        sum=f+s+t
        if sum%n==0:
            print("Incresing and Divisible")
        else:
            print("Incresing but not divisible ")
    else:
        print("All Digits are Different but neither incresing nor Decreasing")
else:
    print("Your Entered More than 3 numbers !")

