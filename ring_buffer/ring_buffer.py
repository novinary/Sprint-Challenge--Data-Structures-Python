'''
A ring buffer is a data structure that is treated as circular although it its implementation is linear. 
A circular buffer is typically used as a data queue. A circular buffer is a popular way to implement a data stream 
because the code can be compact.
'''

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

# The append method adds elements to the buffer.
  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    self.current = self.current % len(self.storage)

# The get method returns all of the elements in the buffer in a list in their given order.
# It should not return any None values in the list even if they are present in the ring buffer.
  def get(self):
    array_to_return = []
    if self.storage != None:
      for i in self.storage:
        if i != None:
          array_to_return.append(i)
    return array_to_return