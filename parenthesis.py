o = ["[","{","("]
c = ["]","}",")"]

s = input("Enter the string: ")
count = 0
for i in range(len(s)):
    if len(s)%2 == 0:
        if s[i] in o:
            for j in range(3):
                if s[i] == o[j]:
                    x = j
            if s[-(i+1)] == c[x]:
                count = 1
            else:
                count = 0
                break
    else:
        break
if count !=0:
    print("True")
else:
    print("False")
    
        
