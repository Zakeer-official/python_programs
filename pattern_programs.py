n = int(input("Enter the no. of rows: "))

print("Pattern 1\n")
for i in range(n):
    print("&"*n)

print("\nPattern 2\n")
for i in range(1,n+1):
    print(str(i)*n)

print("\nPattern 3\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()

print("\nPattern 4\n")
for i in range(n):
    print(chr(65+i)*n)

print("\nPattern 5\n")
for i in range(n):
    for j in range(n):
        print(chr(65+j),end="")
    print()

print("\nPattern 6\n")
for i in range(n,0,-1):
    print(str(i)*n)

print("\nPattern 7\n")
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end="")
    print()

print("\nPattern 8\n")
for i in range(n-1,-1,-1):
    print(chr(65+i)*n)

print("\nPattern 9\n")
for i in range(n):
    for j in range(n-1,-1,-1):
        print(chr(65+j),end="")
    print()

print("\nPattern 10\n")
for i in range(1,n+1):
    print("*"*i)

print("\nPattern 11\n")
for i in range(1,n+1):
        print(str(i)*i)

print("\nPattern 12\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("\nPattern 13\n")
for i in range(1,n+1):
    print(chr(64+i)*i)

print("\nPattern 5\n")
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

print("\nPattern 15\n")
for i in range(n,0,-1):
    print("*"*i)

print("\nPattern 16\n")
for i in range(1,n+1):
    print(str(i)*(n-i+1))

print("\nPattern 17\n")
for i in range(n):
    for j in range(1,n+1-i):
        print(j,end="")
    print()

print("\nPattern 18\n")
for i in range(n):
    print(chr(65+i)*(n-i))

print("\nPattern 19\n")
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end="")
    print()

print("\nPattern 20\n")
for i in range(n,0,-1):
    print(str(i)*i)

print("\nPattern 21\n")
for i in range(n):
    for j in range(n,i,-1):
        print(j,end="")
    print()
    
print("\nPattern 22\n")
for i in range(n,0,-1):
    print(chr(64+i)*i)

print("\nPattern 23\n")
for i in range(n):
    for j in range(n,i,-1):
        print(chr(64+j),end="")
    print()

print("\nPattern 24\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 25\n")
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)

print("\nPattern 26\n")
for i in range(1,n+1):
    print(" "*(n-i)+(str(i)+" ")*i+" "*(n-i))

print("\nPattern 27\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(str(j)+" ",end="")
    print()

print("\nPattern 28\n")
for i in range(1,n+1):
    print(" "*(n-i)+(chr(64+i)+" ")*i+" "*(n-i))

print("\nPattern 29\n")    
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j)+" ",end="")
    print()

print("\nPattern 30\n")
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)

print("\nPattern 31\n")
for i in range(n,0,-1):
    print(" "*(n-i)+(str(i)+" ")*i+" "*(n-i))

print("\nPattern 32\n")
x=1
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    while i:
        print(str(x)+" ",end="")
        x = x+1
        i -= 1
    else:
        x = 1
    print()

print("\nPattern 33\n")
for i in range(n,0,-1):
    print(" "*(n-i)+(chr(64+i)+" ")*i+" "*(n-i))

print("\nPattern 34\n")
x = 1
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    while i:
        print(chr(64+x)+" ",end="")
        x = x+1
        i -= 1
    else:
        x = 1
    print()

print("\nPattern 35\n")
for i in range(1, n+1):
    print(" "*(n-i), "*"*(2*i-1))

print("\nPattern 36\n")
for i in range(1, n+1):
    print(" "*(n-i), str(i)*(2*i-1))

print("\nPattern 37\n")
for i in range(1, n+1):
    print(" "*(n-i), chr(64+i)*(2*i-1))

print("\nPattern 38\n")
for i in range(1, n+1):
    print(" "*(n-i), chr(64+2*i-1)*(2*i-1))

print("\nPattern 39\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(str(j),end="")
    print()

print("\nPattern 40\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(str(j),end="")
    print()

print("\nPattern 41\n")    
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(chr(64+j),end="")
    print()

print("\nPattern 42\n")    
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(chr(64+j),end="")
    print()

print("\nPattern 43\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i-1,-1,-1):
        print(j,end="")
    for k in range(1,i):
        print(k,end="")
    print()

print("\nPattern 44\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    for k in range(1,i):
        print(chr(65+k),end="")
    print()
        
print("\nPattern 45\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()

print("\nPattern 46\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end="")
    for k in range(1,i):
        print(chr(64+k),end="")
    print()

print("\nPattern 47\n")   #red
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()

print("\nPattern 48\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print("*"*(2*j-1))
        break

print("\nPattern 49\n")
for i in range(n,0,-1):
    print(" "*(n-i)+str(i)*(2*i-1))

print("\nPattern 50\n")
for i in range(n,0,-1):
    print(" "*(n-i)+str(2*i-1)*(2*i-1))

print("\nPattern 51\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

print("\nPattern 52\n")
for i in range(n,0,-1):
    print(" "*(n-i)+chr(64+i)*(2*i-1))

print("\nPattern 53\n")
for i in range(n,0,-1):
    print(" "*(n-i)+chr(64+(2*i-1))*(2*i-1))

print("\nPattern 54\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if j == 2*i//2 and j != 2*i-1:
            print(chr(64+j)*2,end="")
        elif j < 2*i-1 or j ==1:
            print(chr(64+j),end="")
    print()

print("\nPattern 55\n") #red
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(str(j),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(str(j),end=" ")
    print()

print("\nPattern 56\n") #red
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 57\n")  #red
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n-1,n-i-1,-1):
        print(str(j),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-1,n-i-1,-1):
        print(str(j),end=" ")
    print()

print("\nPattern 58\n")  #red
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n-i,n):
        print(str(j),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-i,n):
        print(str(j),end=" ")
    print()

print("\nPattern 59\n")  #red
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n-i,n):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-i,n):
        print(chr(65+j),end=" ")
    print()

print("\nPattern 60\n")
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)

print("\nPattern 61\n")
for i in range(1,n+1):
    for j in range(n-1,n-i-1,-1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-1,n-i-1,-1):
        print(j,end="")
    print()

print("\nPattern 62\n")
for i in range(1,n+1):
    for j in range(n-i,n):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i,n):
        print(j,end="")
    print()

print("\nPattern 63\n")
for i in range(1,n+1):
    print(chr(64+n-i+1)*i)
for i in range(n-1,0,-1):
    print(chr(64+n-i+1)*i)

print("\nPattern 64\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+n-j+1),end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print(chr(64+n-j+1),end="")
    print()

print("\nPattern 65\n")
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(chr(64+n-j+1),end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(chr(64+n-j+1),end="")
    print()

print("\nPattern 66\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 67\n")
for i in range(1,n+1):
    print(" "*(n-i)+(str(i)+" ")*i)

print("\nPattern 68\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print((str(j)),end=" ")
    print()

print("\nPattern 69\n")
for i in range(1,n+1):
    print(" "*(n-i)+(chr(64+i)+" ")*i)

print("\nPattern 70\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print("\nPattern 71\n")
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 72\n")
for i in range(n,0,-1):
    print(" "*(n-i)+(str(i)+" ")*i)

print("\nPattern 73\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print((str(j)),end=" ")
    print()

print("\nPattern 74\n")
for i in range(n,0,-1):
    print(" "*(n-i)+(chr(64+i)+" ")*i)

print("\nPattern 75\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(chr(64+j),end=" ")
    print()

print("\nPattern 76\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print("\nPattern 77\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 78\n")
for i in range(1,n+1):
    print(" "*(n-i)+(str(i)+" ")*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+(str(i)+" ")*i)

print("\nPattern 79\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print((str(j)),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-i+1,n+1):
        print((str(j)),end=" ")
    print()

print("\nPattern 80\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print((str(j)),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print((str(j)),end=" ")
    print()

print("\nPattern 81\n")
for i in range(1,n+1):
    print(" "*(n-i)+(chr(64+i)+" ")*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+(chr(64+i)+" ")*i)

print("\nPattern 82\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-i+1,n+1):
        print(chr(64+j),end=" ")
    print()

print("\nPattern 83\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n-i+1,n+1):
        print(str(j),end="")
    for k in range(n-1,n-i,-1):
        print(str(k),end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n-i+1,n+1):
        print(str(j),end="")
    for k in range(n-1,n-i,-1):
        print(str(k),end="")
    print()

print("\nPattern 84\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n,n-i,-1):
        print(str(j),end="")
    for k in range(n-i+2,n+1):
        print(str(k),end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(n,n-i,-1):
        print(str(j),end="")
    for k in range(n-i+2,n+1):
        print(str(k),end="")
    print()

print("\nPattern 85\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(n,n-i,-1):
        if j == n or j == n-i+1:
            print("*"+" "*(i-1),end="")
        else:
            print(end=" ")
    print()

print("\nPattern 86\n")
for i in range(1,n+1):
    print(" "*(n-i)+str(i)+" "*(2*i-3)+(" " if str(i) == str(1) else str(i)))

print("\nPattern 87\n")
for i in range(1,n+1):
    print(" "*(n-i)+str(n-i+1)+" "*(2*i-3)+(" " if str(i) == str(1) else str(n-i+1)))

print("\nPattern 88\n")
for i in range(1,n+1):
    print(" "*(n-i)+chr(64+n-i+1)+" "*(2*i-3)+(chr(64+n-i+1) if str(chr(64+n-i+1)) != str("E") else " " ))

print("\nPattern 89\n")
for i in range(1,n+1):
    print(" "*(n-i)+chr(64+i)+" "*(2*i-3)+(chr(64+i) if str(chr(64+i)) != str("A") else " " ))

print("\nPattern 90\n")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(n,n-i,-1):
        if j == n or j == n-i+1:
            print("*"+" "*(i-1),end="")
        else:
            print(end=" ")
    print()

print("\nPattern 91\n")
for i in range(n,0,-1):
    print(" "*(n-i)+str(n-i+1)+" "*(2*i-3)+(" " if str(n-i+1) == str(5) else str(n-i+1)))

print("\nPattern 92\n")
for i in range(n,0,-1):
    print(" "*(n-i)+str(i)+" "*(2*i-3)+(" " if str(i) == str(1) else str(i)))

print("\nPattern 93\n")
for i in range(n,0,-1):
    print(" "*(n-i)+chr(65+i-1)+" "*(2*i-3)+(" " if str(chr(65+i-1)) == str("A") else chr(65+i-1)))

print("\nPattern 94\n")
for i in range(n,0,-1):
    print(" "*(n-i)+chr(65+n-i)+" "*(2*i-4)+(" " if str(chr(65+n-i)) == str("D") or str(chr(65+n-i)) == str("E") else chr(65+n-i)))

print("\nPattern 95\n")
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*n)

print("\nPattern 96\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i+" "*(n-i)+"* "*i)

print("\nPattern 97\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2 == 1:
            if j%2 == 1:
                print("1",end="")
            else:
                print("0",end="")
        else:
            if j%2 == 1:
                print("0",end="")
            else:
                print("1",end="")
    print()

print("\nPattern 98\n")
for i in range(1,n+1):
    print(" "*(2*n-i+2)+"* "*i)
for i in range(3,2*n):
    print(" "*(2*n-i+2)+"* "*i)
for i in range(4,2*n+3):
    print(" "*(2*n-i+2)+"* "*i)
for i in range(1,2*n-2):
    print(" "*(2*n-1)+"* "*3)

print("\nPattern 99\n")
for i in range(1,n+1):
    print(" "*(2*n-i)+"* "*i)
for i in range(1,n+1):
    print(" "*(n-i+1)+"* "*i+" "*(n-i)+"* "*i)

print("\nPattern 100\n")
for i in range(1,n+1):
    print("*"*(2*i))
    print("*"*(2*i))

print("\nPattern 102\n")  #tripod triange pattern
for i in range(1,n+1):
    print(" "*(2*n-i+1)+"* "*i)
for i in range(1,n+1):
    print(" "*(n-i+1)+"* "*i+" "*(n-i)+" "*(n-i)+"* "*i)
