'''
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.
Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

Tasks

You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.
'''

'''
Task 1:
    Input: single integer representing number of available blocks
    Output: single integer representing number of blocks left over
    Rules:
        Top layer is a single block
        Each block above layer 1 must be supported by 4 blocks

    Visualizing the problem:
        5 Blocks - 0 blocks left over
        Layer 1             Layer 2
          __   __
         |__| |__|             __
          __   __             |__|
         |__| |__|

        8 Blocks - fails because top layer is not single block
                 - it would produce a 5-block valid structure with 3 blocks leftover
        Layer 1               Layer 2
          __   __   __
         |__| |__| |__|       __   __
          __   __   __       |__| |__|
         |__| |__| |__|

        14 Blocks - 0 blocks left over
        Layer 1               Layer 2       Layer 3
          __   __   __
         |__| |__| |__|       __   __
          __   __   __       |__| |__|        __
         |__| |__| |__|       __   __        |__|
          __   __   __       |__| |__|
         |__| |__| |__|
'''

'''
Task 2: Test cases

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
'''

'''
Task 3: Data Structure
Integer
'''

'''
Task 4: Algorithm

set layer to 1
set blocks_required to 1
increment layer and see what the blocks required would be
if blocks supplied <= next layer blocks required
    return blocks supplied - blocks required
else
    increment layer

'''

'''
Task 5: Code

layer = 1
blocks_required = 1
while True
    next_layer = layer + 1
    next_required = blocks_required + next_layer ** 2
    if blocks_supplied <= next_required:
        break
    else:
        layer += 1
        blocks_required += layer ** 2
return block_supplied - blocks_required
'''

def calculate_leftover_blocks(supply):
    layer = 0

    while True:
        if (supply - layer ** 2) < 0:
            break

        supply -= layer ** 2
        layer += 1

    return supply

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
