class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class SLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.node_amount = 1

    def listprint(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next_node
    # Growing a reverse-order LinkedList
    def insertReverse(self, data):
        # Create next new node
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
        # Extend linked list
        else:
            # Point to next new node
            new_node.next_node = self.head
            # Save newly grown linked list
            self.head = new_node
        # Update node count
        self.node_amount +=1

    # Growing a forward-order LinkedList
    def insertForward(self, data):
        # Create next new node
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
        # Extend linked list
        else:
            # Point to next new node
            previous_head = self.head
            while (previous_head.next_node):
                previous_head = previous_head.next_node
            previous_head.next_node = new_node
        # Update node count
        self.node_amount += 1
    # Return LinkedList size
    def size(self):
        return self.node_amount

mylist= SLinkedList()
T=int(input())
for i in range(0,T):
    data = int(input())
    mylist.head = Node(data)
# Print all values stored in Linked List
mylist.listprint()
print("\n",mylist.size(), "Yay")