#__author__ : "Girish Fedram"


class Node:
    """
    A node in a doubly-linked list.
    """

    def __init__(self, data=None, next=None, prev=None):

        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList:

    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """

        #create new node first
        new_node = Node(data, next=None, prev=None)

        if self.head:

            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

        print(data, "Preppended")

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        #create new node first
        new_node = Node(data, next=None, prev=None)

        curr = self.head

        #traverse
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
        print( data , "Appended")

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """

        curr = self.head

        while curr and curr.data != key:
            curr = curr.next

        return curr

    def remove_element(self, value):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """

        curr = self.head
        prev = None

        while curr and curr.data != value:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
            nn = curr.next
            nn.prev = prev

        curr.next = None
        curr.prev = None
        print("Removed")

    def reverse(self):
        curr = self.head
        prev_node = None

        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev


dl = DoublyLinkedList()

print(dl)

dl.prepend(10)
print(dl)

dl.prepend(40)
dl.prepend(30)
print(dl)

dl.append(600)
dl.append(1400)
print(dl)

print(dl.find(1400)) #prints 1400
print(dl.find(1401))  #prints None as element doesn't exists

print(dl)
dl.remove_element(30)
print(dl)

print(dl)
print(dl.reverse(), dl)
