'''
Alyssa was asked to write an implementation of a rolling buffer. You can add
and remove elements from a rolling buffer. However, once the buffer becomes
full, any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:
'''

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    'def 1'
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    'def 2'
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

'''
The difference is that append will mutate buffer, so if it is used anywhere
else in the code, it will be changed.
The second function creates a new local variable in it's scope and concatenates
the buffer argument with the new element and returns that new buffer object
'''
