start = int(input()) # 10
end = int(input()) # 50

for i in range(start, end + 1): #10 11 12 13 14 15 16 17 

    temp = i # temp=10
    n = i # n=10
    r = 0

    while n > 0: # 10>0 T
        d = n % 10 # 0
        r = r * 10 + d 
        n = n // 10

    if temp == r:
        print(temp, end=" ")
