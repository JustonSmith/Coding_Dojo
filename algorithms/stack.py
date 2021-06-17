class Stack(): 
    def __init__(self): # What data type will allow for the LIFO principle? [LIST] # list(array) or SLL
        self.data = []
        pass

    def is_empty(self): # Return whether the stack is empty.
        print(self.data)
        if len(self.data) -1 == 0:
            return True
        else:
            return False
        return self.data
        pass

    def size(self): # Return the number of stacked values
        return len(self.data)
        pass

    def top(self): # Return (not remove) the stack’s top value.
        
        pass

    def push(self, val): # Create push(val) that adds val to our stack.
        
        pass

    def pop(self): # Create pop() to remove and return the top val.
        
        pass

    def contains(self, val): # Return whether given val is within the stack.
        
        pass