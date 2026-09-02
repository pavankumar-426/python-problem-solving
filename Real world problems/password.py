n=input()
upper=0
lower=0
special=0
num=0
specialc="!@#$&"
for i in n:
    if "A"<=i<="Z":
        upper=upper+1
    elif"a"<=i<="b":
        lower=lower+1
    elif "0"<=i<="9":
        num=num+1
    elif i=='@'or i=='!'or i=='#'or i=='$'or i=='&':
        special=special+1 
if upper>=1 and lower>=1 and special>=1 and num>=1:
    print("Strong password")
else:
    print("Not strong Password")
        