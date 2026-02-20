# #5 → 10 → 20 → 30 → None


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# a = Node(4)
# head = Node(10)

# second = Node(20)
# third = Node(30)

# head.next = second
# second.next = third 


# a.next = head
# head =  a















class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

first = Node(3)
second = Node(5)
third = Node(2)

head = first
first.next = second
second.next = third
third.next = None

## insertion at beginning
Zero = Node(1)
Zero.next = first
head = Zero

#insertion at end 
Last = Node(6)
Last.next = None
third.next = Last

#insertion at mid
Mid = Node(34)
second.next = Mid
Mid.next = third


current = head
while current:
    print(current.data)
    current = current.next











