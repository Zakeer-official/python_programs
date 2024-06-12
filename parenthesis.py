
""" parenthesis using lists with
                        more complexity
"""

o = ["[","{","("]
c = ["]","}",")"]

s = input("Enter the string: ")
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


""" parenthesis using dictionaries with
                        less complexity 0(n)
"""

d ={"]" : "[", ")" : "(", "}":"{"}
s = input("Enter the string: ")
l = []
for i in range(len(s)):
    if len(s)%2 == 0:
        if s[i] in list(d.values()):
            l.append(s[i])
        elif s[i] in list(d.keys()):
            if d[s[i]] == l[-1]:
                l.pop()
        else:
            break
    else:
        break
if len(l) == 0:
    print("True")
else:
    print("False")
