#strong number

n=int(input("Enter the number: "))
temp=n
s=0
while n>0:
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n=n//10
if temp==s:
    print("strong number")
else:
    print("Not strong number")