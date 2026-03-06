class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None


    def insert_at_end(self,data):
       
       new_node = Node(data)

       if self.head is None:
           self.head = new_node
           return

       current = self.head
       while current.next:
           current = current.next

       current.next = new_node
 
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


ll = linkedlist()
ll.insert_at_end(4)
ll.insert_at_end(3)
ll.insert_at_end(6)

ll.print()
