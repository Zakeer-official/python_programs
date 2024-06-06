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
