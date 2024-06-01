n = int(input("Enter Number: "))
flag = 0
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j == 0:
            break
    if i==j:
        print(i,end=",")
        flag += 1 
print("\nTotal prime numbers are : ",flag)
