#__author__ : "Girish Fedram"

class Node:

    def __init__(self, data=None, next=None):

        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):

        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ",".join(nodes) + ']'


    def prepend(self, data):
        self.head = Node(data=data, next=self.head)
        print("Element prepended..!!")

    def append(self, data):

        #check for the empty list
        if not self.head:
            print("head node added")
            self.head = Node(data=data, next=None)
            return

        #traverse till end of the list
        curr = self.head
        while curr.next:
            curr = curr.next

        #add new node at last
        curr.next = Node(data=data, next=None)
        print("Element appended..!!")

    def find(self, key):
        curr = self.head

        while curr and curr.data != key:
            curr = curr.next

        #will be none if not found
        return curr

    def remove(self, key):

        if self.head:

            curr = self.head
            prev = None

            while curr and curr.data != key:
                prev = curr
                curr = curr.next

            if prev is None:
                self.head = curr.next
            elif curr:
                prev.next = curr.next
                curr.next = None
        print("Element removed..!!")

    def reverse(self):

        curr = self.head
        prev_node = None
        next_node = None


        while curr:

            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node



ll = SinglyLinkedList()

print(ll)  #empty list

ll.append(10)
ll.append(40)
ll.append(30)
ll.append("Girish")

print(ll)  #[10,40,30,'Girish']

print(ll.find(45))
print(ll.reverse(), ll)
print(ll)
ll.prepend("addfadf")
ll.append("zzzzzzz")
print(ll)