class queue:
    def __init__(self,n):
        self.q = []
        self.n = n
    def isempty(self):
        return len(self.q) == 0
    def isfull(self):
        return len(self.q) == self.n
    def enqueue(self,y):
        if self.isfull():
            raise "Queue Overflow"
        else:
            self.q.insert(0,y)
    def dequeue(self):
        if self.isempty():
            raise "Stack Underflow"
        else:
            self.q.pop()
    
    def print(self):
        print(self.q)
        



#Example
x = 10
a = queue(x)

a.enqueue(5)
a.enqueue(10)
a.dequeue()
a.print()
    
