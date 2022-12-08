"""
Solves https://adventofcode.com/2022/day/5
Part 1: It got the stack data structure correct but I had to add an iterator to move_crates(). 
I also had to add significant changes to the parser and other things.
Part 2: Interestingly, the sentence "the ability to pick up and move multiple crates at once" made it fix some of the 
things I had to add manually in Step 1! It did not get the ordering right, so I had to reverse the list. Otherwise, I 
just had to mix it together with my parser from Step 1.
"""

# Part 1:

class Stack:
    def __init__(self):
        self.crates = []

    def add_crate(self, crate):
        self.crates.append(crate)

    def remove_crate(self):
        return self.crates.pop()

    def get_top_crate(self):
        return self.crates[-1]

class Stacks:
    def __init__(self):
        self.stacks = []

    def move_crates(self, num_crates, from_stack, to_stack): # Modified
        for _ in range(num_crates): # Added
            crate = self.stacks[from_stack].remove_crate()
            self.stacks[to_stack].add_crate(crate)

    def get_top_crates(self):
        return [stack.get_top_crate() for stack in self.stacks]

with open('5.txt') as f:
    lines = f.readlines()

# Parse the input
stacks = Stacks()
empty_line_idx = 0  # Added
for i, line in enumerate(lines):
    if line.startswith(" 1"):  # Added
        empty_line_idx = i+1  # Added
        break  # Added
    crate_line = line.replace("    ", "[-]").replace("\n","").replace(" ", "")  # Added
    for j, crate in enumerate(crate_line[k:k+3] for k in range(0, len(crate_line), 3)):  # Added
        if i == 0:  # Added
            stack = Stack()  # Added
            stacks.stacks.append(stack)  # Added
        else:  # Added
            stack = stacks.stacks[j]  # Added
        if crate != '[-]':  # Added
            stack.crates.append(crate)  # Added

for stack in stacks.stacks:  # Added
    stack.crates = list(reversed(stack.crates))  # Added


movement_instructions = [line.strip().split() for line in lines[empty_line_idx+1:]] # Modified


# Apply the movement instructions
for instruction in movement_instructions:
    crates = int(instruction[1])  # Added
    from_stack = int(instruction[3]) - 1  # Modified
    to_stack = int(instruction[5]) - 1 # Modified
    stacks.move_crates(crates, from_stack, to_stack) # Modified

# Get the top crates of each stack
top_crates = stacks.get_top_crates()

# Print the result
print(''.join(top_crates).replace("[", "").replace("]", "")) # Modified


# Part 2:

import re

class Stack:
    def __init__(self):
        self.crates = []

    def add_crate(self, crate):
        self.crates.append(crate)

    def remove_crate(self):
        return self.crates.pop()

    def get_top_crate(self):
        return self.crates[-1]


class Stacks:
    def __init__(self):
        self.stacks = []

    def move_crates(self, from_stack, to_stack, num_crates):
        crates = [self.stacks[from_stack].remove_crate() for _ in range(num_crates)]
        for crate in reversed(crates):  # Modified
            self.stacks[to_stack].add_crate(crate)

    def get_top_crates(self):
        return [stack.get_top_crate() for stack in self.stacks]


# Read the input
with open('5.txt') as f:
    text = f.read()
lines = text.splitlines()

# Parse the input
stacks = Stacks()
empty_line_idx = 0  # Added
for i, line in enumerate(lines):
    if line.startswith(" 1"):  # Added
        empty_line_idx = i+1  # Added
        break  # Added
    crate_line = line.replace("    ", "[-]").replace("\n","").replace(" ", "")  # Added
    for j, crate in enumerate(crate_line[k:k+3] for k in range(0, len(crate_line), 3)):  # Added
        if i == 0:  # Added
            stack = Stack()  # Added
            stacks.stacks.append(stack)  # Added
        else:  # Added
            stack = stacks.stacks[j]  # Added
        if crate != '[-]':  # Added
            stack.crates.append(crate)  # Added

for stack in stacks.stacks:  # Added
    stack.crates = list(reversed(stack.crates))  # Added


movement_instructions = [line.strip().split() for line in lines[empty_line_idx+1:]] # Modified


# Apply the movement instructions
for instruction in movement_instructions:
    crates = int(instruction[1])  # Added
    from_stack = int(instruction[3]) - 1  # Modified
    to_stack = int(instruction[5]) - 1  # Modified
    stacks.move_crates(from_stack, to_stack, crates)  # Modified

# Get the top crates of each stack
top_crates = stacks.get_top_crates()

# Print the result
print(''.join(top_crates).replace("[", "").replace("]", ""))
