class stack:
    def __init__(self,n):
        self.st = []
        self.n = n
    def isempty(self):
        return len(self.st) == 0
    def isfull(self):
        return len(self.st) == self.n
    def push(self,y):
        if self.isfull():
            raise "Stack Overflow"
        else:
            self.st.append(y)
    def pop(self):
        if self.isempty():
            raise "Stack Underflow"
        else:
            self.st.pop()
    
    def print(self):
        print(self.st)
        



#Example
x = 10
a = stack(x)

a.push(5)
a.push(10)
a.pop()
print(a.print())
    
