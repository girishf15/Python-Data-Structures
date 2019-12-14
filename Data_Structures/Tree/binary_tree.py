#__author__ : "girish"

class BinaryNode:

    def __init__(self, data=None):

        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def insert(self, data):

        #create node first
        new_node = BinaryNode(data)

        #check for value with parent node
        if self.data:

            if data < self.data:

                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printInorder(self):

        if self.data:
            if self.left:
                self.left.printInorder()
            print(self.data, end=" ")
            if self.right:
                self.right.printInorder()

root = BinaryNode(50)
#root.printInorder()
root.insert(10)
root.insert(60)
root.insert(30)
root.insert(70)
root.printInorder()