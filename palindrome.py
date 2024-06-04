n = int(input("Enter the number: "))
lst =[p for p in range(n) if int (str (p)[::-1]) == p] #it stores palindrome numbers in the list upto n number
  
print (lst)

