'''
A circular buffer is a collection of objects stored in a buffer that is treated as though it is connected end-to-end in a circle. When an object is added to this circular buffer, it is added to the position that immediately follows the most recently added object, while removing an object always removes the object that has been in the buffer the longest.

This works as long as there are empty spots in the buffer. If the buffer becomes full, adding a new object to the buffer requires getting rid of an existing object; with a circular buffer, the object that has been in the buffer the longest is discarded and replaced by the new object.
'''

'''
Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide the following methods:

put: Add an object to the buffer
get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.
You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).
'''

# Only arg is size of buffer
# Initialize buffer so ever element is None
# set current_element to be index 0
# set oldest_element to be index 0

# on put command, load obj into current_element, if current_element is > buffer size, current_element = 0
#                   if current_element = 0 and buffer[current_element] != None, oldest_element += 1
# on get command, remove and return oldest element,

class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self.initialize_buffer()
        self._put_counter = 0
        self._get_counter = 0

    def initialize_buffer(self):
        self._buffer = []
        for _ in range(self._buffer_size):
            self._buffer.append(None)

    def put(self, obj):
        idx = self._put_counter % self._buffer_size
        self._buffer[idx] = obj
        self._put_counter += 1
        self.decrement_get_counter()

    def get(self):
        idx = self.oldest_idx()
        obj = self._buffer[idx]
        self._buffer[idx] = None
        self.increment_get_counter()
        return obj

    def increment_get_counter(self):
        if self._buffer.count(None) != self._buffer_size:
            self._get_counter += 1
        else:
            self._get_counter = 0
            self._put_counter = 0

    def decrement_get_counter(self):
        if self._get_counter > 0 and self._put_counter > self._buffer_size:
            self._get_counter -= 1

    def oldest_idx(self):
        if self._put_counter < self._buffer_size: return self._get_counter
        oldest = (self._put_counter % self._buffer_size) + (self._get_counter % self._buffer_size)
        return oldest % self._buffer_size

    def display_stats(self):
        idx = self.oldest_idx()
        print(f"""
            == Get Operation:
            current buffer: {self._buffer}
            put_counter: {self._put_counter}
            get_counter: {self._get_counter}
            oldest_idx: {idx}
            object returned: {self._buffer[idx]}
        """)


print('-- Circular Buffer of Size 3 ==')
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

print('-- Circular Buffer of Size 4 ==')
buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
