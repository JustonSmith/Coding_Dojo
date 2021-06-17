class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class SLQueue():
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        newnode = Node(value)
        if self.front != None:
            self.back.next = newnode
            self.back = self.back.next
        else:
            self.front = newnode
            self.back = self.front
        # add the given value to the end of the queue
        

    def dequeue(self):
        if self.front != None:
                tempnode = self.front
                self.front = self.front.next
                if self.front == None:
                    self.back = None
        else:
            return None
        # remove and return the first node of the queue
        
        

    def front(self):
        # return the front value of the queue
        pass

    def contains(self, value):
        # return a boolean on whether or not the value is found in the queue
        pass

    def is_empty(self):
        # return a boolean on whether or not the queue contains values
        pass

    def size(self):
        # return the number on values in the queue
        pass