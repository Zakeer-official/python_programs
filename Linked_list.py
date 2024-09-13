
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
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'
    
    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None :
            return 'Empty'
        self.head = self.head.next
        self.n = self.n - 1

    def delete_tail(self):
        if self.head == None :
            return 'Empty'
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1

    def delete_value(self,value):
        if self.head == None :
            return 'Empty'
        if self.head.data == value :
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return 'Item not found'
        else:
            curr.next = curr.next.next

    def search_value(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "Item not found"

    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
        return 'IndexError'


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
a.insert_after(3,4)
print(a.traverse())