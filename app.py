print('Hello World')

class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    def add(self, val):
        temp = self.head
        if temp is None:
            return "Linked List Does not exist"
        temp.next = Node(val)
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

node1 = Node(1)

ll1 = LinkedList(node1)

ll1.add(2)

ll1.print_list()