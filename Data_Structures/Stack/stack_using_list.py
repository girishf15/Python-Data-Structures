# __author__ : girish

'''
Stack in Python can be implemented using following ways:

    list
    collections.deque
    queue.LifoQueue
'''


class StackTest:

    def __init__(self, stack=[], length=0):
        self.stack = []
        self.stack_length = length

    def push(self, element):
        if len(self.stack) == self.stack_length:
            print("Stack is Full")
        else:
            self.stack.append(element)

    def pop(self):

        if len(self.stack):
            return self.stack.pop()
        else:
            print("Stack is Empty")

    def __repr__(self):
        return str(self.stack)


ss = StackTest(length=3)

ss.push(10)
ss.push(20)
ss.push(30)
ss.push(410)
print(ss)

ss.pop()
ss.pop()
ss.pop()
print(ss)
ss.pop()
