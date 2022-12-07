"""
Part 1: Got most of the logic right. Forgot to handle the case for "cd .." and include a parent property in Node. Most 
indicies were wrong as it overlooked '$'. I also had to add the function calls in the end because ChatGPT ran out of 
reached its output limit.
Part 2: I had to add some function calls but otherwise the logic was correct. It also didn't use the node class but a 
dictionary instead which I had to swap out.
"""

# Part 1

class Node:
    def __init__(self, name, is_dir=False, size=0, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = []
        self.parent = parent  # Added


def build_filesystem_tree(input_lines):
    # Initialize the root node
    root = Node("/", is_dir=True)

    # Keep track of the current directory
    current_dir = root

    # Iterate through the lines of input
    reading_files = False
    for i, line in enumerate(input_lines):

        # Split the line into tokens
        tokens = line.strip().split(" ")

        if reading_files:
            if tokens[0] == "$":
                reading_files = False
            else:
                # Following logic was moved
                name = tokens[1]
                size = int(tokens[0]) if tokens[0].isdigit() else None

                # Create a node for the file or directory
                node = Node(name, is_dir=size is None, size=size, parent=current_dir)

                # Add the node as a child of the current directory
                current_dir.children.append(node)
                continue

        # Handle the "cd" command
        if tokens[1] == "cd":
            # Handle the special case of switching to the root directory
            if tokens[2] == "/":
                current_dir = root
            elif tokens[2] == "..":  # Added special case
                current_dir = current_dir.parent
            else:
                # Otherwise, move into the specified child directory
                child_dir = next((child for child in current_dir.children if child.name == tokens[2]), None)
                if child_dir:
                    current_dir = child_dir

        # Handle the "ls" command
        elif tokens[1] == "ls":
            # Parse the files and directories in the current directory
            reading_files = True  # Added

    # Return the root node of the filesystem tree
    return root


def find_directories_with_total_size_at_most(root, size_limit):
    # Initialize a set to hold the names of directories with total size at most size_limit
    directories = set()

    # Define a recursive helper function to traverse the tree and calculate the total size of each directory
    def traverse(node):
        # Initialize the total size of the directory to 0
        node.size = 0

        # Traverse the children of the node
        for child in node.children:
            # Recurse into child directories
            if child.is_dir:
                traverse(child)

            # Add the size of the child to the total size of the directory
            node.size += child.size

        # Add the directory to the set of directories with total size at most size_limit
        if node.size <= size_limit:
            directories.add(node)

    # Call the helper function to traverse the tree and calculate the total sizes of each directory
    traverse(root)

    # Return the set of directories with total size at most size_limit
    return directories


# Added these function calls
input_lines = open("8.txt").readlines()
root = build_filesystem_tree(input_lines)
directories = find_directories_with_total_size_at_most(root, 100000)
total_size = 0
for dir in directories:
    total_size += dir.size
print(total_size)


# Part 2

def smallest_dir_to_free_up_space(required_space, dirs):
    # Find the directories with a size equal to or greater than the required space
    eligible_dirs = [d for d in dirs if d.size >= required_space]

    # Sort the eligible directories by size
    eligible_dirs.sort(key=lambda d: d.size)

    # Return the smallest eligible directory
    return eligible_dirs[0] if eligible_dirs else None


disk_space = 70000000
required_space = 30000000
root = build_filesystem_tree(input_lines)  # Added
all_dirs = find_directories_with_total_size_at_most(root, 0)  # Added
unused_space = disk_space - root.size  # Added
space_needed = required_space - unused_space  # Added
dirs = find_directories_with_total_size_at_most(root, disk_space)  # Added
smallest_dir = smallest_dir_to_free_up_space(space_needed, dirs)

if smallest_dir:
  print(f'The smallest directory that, if deleted, would free up enough space to run the update is {smallest_dir.name} with size {smallest_dir.size}.')
else:
  print('There are no directories that, if deleted, would free up enough space to run the update.')
  