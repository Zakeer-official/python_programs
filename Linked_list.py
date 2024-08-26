
class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        new_node = Node(value)                       #new_node
        new_node.next = self.head                    #created connection
        self.head = new_node                         #reassigned head
        self.n = self.n + 1

    def insert_tail(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self,after,value):
        new_node = Node(value)


    def traverse(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

a = LinkedList()
a.insert_head(1)
a.insert_head(2)
a.insert_tail(3)
print(a.traverse())