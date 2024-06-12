o = ["[","{","("]
c = ["]","}",")"]

s = input("Enter the string: ")
count = 0
l = []
for i in range(len(s)):
    if len(s)%2 == 0:
        if s[i] in o:
            l.append(s[i])
        else:
            for j in range(3):
                if s[i] == c[j]:
                    m = j
            if l[-1] == o[m]:
                l.pop()
    else:
        break
if len(l) == 0:
    print("True")
else:
    print("False")
    
        

