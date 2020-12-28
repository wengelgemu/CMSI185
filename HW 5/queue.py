'''
queue.py
Name: Wengel Gemu
Collaborators:
Date: October 5th, 2019
Description:
'''

#### our QueueNode class ####
class QueueNode(object):
    def __init__(self, data): # self refers to the Queue object
    	# Queues have two attributes, data and next_node
        self.data = data
        self.next_node = None
        new_node = self.next_node

#### Write your Queue class here ####
class Queue(object):
    """Queue object
    Attributes: head - alias to the node at the front of the queue
                tail - alias to the node at the back of the queue
    """

    def __init__(self, head, tail):
        """Initialize an empty queue"""
        # TODO: initialize self.head and self.tail here
        self.head = head
        self.tail = tail

    def is_empty(self):
        """Check if the queue is empty"""
        # TODO: your code here
        # return true or false for is the list is empty or not
        return (self.head == None)

    def enqueue(self, data):
        """Add a node containing data to the back of the queue"""
        node = QueueNode(data)
        # TODO: your code here
        # if statement checking status of queue and adding data
        if self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = self.tail.next_node


    def dequeue(self):
        """Remove the node at the front of the queue and return its data"""
        # this is an example of how to raise an IndexError
        while self.is_empty():
            raise IndexError("dequeue from empty queue")
        # TODO: your code here
        while self.is_empty() == False:
            data = self.head.data
            self.head = self.head.next_node
            return data


    def peek(self):
        """Look at the node at the front of the queue without removing it"""
        # TODO: your code here
        # you will need to raise another IndexError here
        while self.is_empty():
            raise IndexError("dequeue from empty queue")
        # print(self.head)
        while self.is_empty() == False:
            return self.head.data


# Test out a Queue object where we add and remove nodes
print("Make a queue")
q = Queue(None, None)
print("Queuing item hi")
q.enqueue("hi")
print("First item is", q.peek())
# print("Queuing item hello")
q.enqueue("hello")
print("First item is", q.peek())
print("Dequeing item", q.dequeue())
print("First item is",q.peek())
# print("Queuing item howdy")
q.enqueue("howdy")
# print("Queuing item yo")
q.enqueue("yo")
# print("is_empty() returns", q.is_empty())
print("Dequeing item", q.dequeue())
# EXTRA check
print("First item is",q.peek())
print("Dequeing item", q.dequeue())
# EXTRA check
print("First item is",q.peek())
# print("Dequeing item", q.dequeue())
# print("is_empty() returns", q.is_empty())
