class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class SLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.node_amount = 1
    # Print data points from each Node connected from the head Node
    def listprint(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            if current.next_node:
                current = current.next_node
            else:
                break
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
    # Removing a Node and connecting it to the last node
    def removeDupicates(self):
        current = self.head
        duplicates_found = False
        while current:
            # Find the data and its corresponding node
            try:
                if current.data == current.next_node.data:
                    duplicates_found = True
                    current.next_node = current.next_node.next_node
                else:
                    current = current.next_node
            except:
                break
        # Print new list cleaned of duplicates
        if duplicates_found:
            print("\nDuplicate-free list:", end=' ')
            mylist.listprint()

mylist= SLinkedList()
T=int(input())
for i in range(0,T):
    data = int(input())
    #mylist.head = Node(data)
    mylist.insertForward(data)
# Print all values stored in Linked List
mylist.listprint()
mylist.removeDupicates()
print("\n",mylist.size(), "Yay")