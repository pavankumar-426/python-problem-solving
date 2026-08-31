# Amstrong number 

n=int(input())
s=0
d=0
temp=n
while n>0: #153>0:T              #15>0: T       #1>0:  
    d=n%10  #d=153%10=3         #d=15%10=5      #d=1%1=1 
    s=s+d*d*d   #s=0+3*3*3=27   #s=27+125=152   #s=152+1=153
    n=n//10 # n=153//10=15      #n=15//10=1
if temp==s: #153==153: T
    print("Astrong Number") # Amstrong 
else:
    print("Not Amstrong number ")
