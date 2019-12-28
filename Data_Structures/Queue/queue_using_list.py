class Queue:

    # __init__ function
    def __init__(self, capacity):
        self.front = self.rear = -1
        self.size = 0
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):

        if self.isFull():
            print("Full")
            return

        if self.size == 0:
            self.front += 1

        self.rear += 1
        self.Q[self.rear] = item
        self.size += 1
        print("%s enqueued to queue" % str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("%s dequeued from queue" % str(self.Q[self.front]))

        self.front += 1
        self.size -= 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])

    def __repr__(self):
        return str(self.Q)


# Driver Code
if __name__ == '__main__':

    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)

    queue.DeQueue()

    queue.que_front()
    queue.que_rear()
