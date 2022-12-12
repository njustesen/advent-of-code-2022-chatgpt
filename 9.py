# Part 1:

def tail_position(motions):
  # Initialize the position of the head and tail
  head_row = 0
  head_col = 0
  tail_row = 0
  tail_col = 0

  # Initialize the previous position of the head
  prev_head_row = 0
  prev_head_col = 0

  # Initialize the set of visited positions
  visited_positions = set()
  visited_positions.add((tail_row, tail_col))
  
  # Loop through the motions
  for m in motions:
    motion = m.strip().split(" ")
    for i in range(int(motion[1])):
      # Store the previous position of the head
      prev_head_row = head_row
      prev_head_col = head_col
      # Move the head in the specified direction
      if motion[0] == 'R':
        head_col += 1
      elif motion[0] == 'L':
        head_col -= 1
      elif motion[0] == 'U':
        head_row -= 1
      elif motion[0] == 'D':
        head_row += 1
  
      # Update the position of the tail
      if abs(head_row - tail_row) > 1 or abs(head_col - tail_col) > 1:
        # If the tail is more than one step away from the head, move it to the head's previous position
        tail_row = prev_head_row
        tail_col = prev_head_col
  
      # Add the current position of the tail to the set of visited positions
      visited_positions.add((tail_row, tail_col))
  
  # Return the number of unique positions the tail has visited
  return len(visited_positions)

# Read the series of motions from the input
motions = []
for line in open("9.txt").readlines():
  if line == '':
    break
  motions.append(line)

# Calculate the position of the tail
n_visited_positions = tail_position(motions)

# Print the position of the head and tail
print(n_visited_positions)


# Part 2

def tail_position(motions):
  # Initialize the position of the head and tail
  knots = [[0, 0] for i in range(10)]

  # Initialize the set of visited positions
  visited_positions = set()
  visited_positions.add((knots[-1][0], knots[-1][1]))

  # Loop through the motions
  for m in motions:
    motion = m.strip().split(" ")
    for i in range(int(motion[1])):

      prev_knot = [knots[0][0], knots[0][1]]

      # Move the head in the specified direction
      if motion[0] == 'R':
        knots[0][0] += 1
      elif motion[0] == 'L':
        knots[0][0] -= 1
      elif motion[0] == 'U':
        knots[0][1] -= 1
      elif motion[0] == 'D':
        knots[0][1] += 1

      # Update the position of each knot in the rope
      
      for i in range(1, 10, 1):
        head = knots[i-1]
        tail = knots[i]
        # Update the position of the tail
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
          new_prev_knot = [tail[0], tail[1]]
          # If the tail is more than one step away from the head, move it to the head's previous position
          tail[0] = prev_knot[0]
          tail[1] = prev_knot[1]
          prev_knot = new_prev_knot

      # Add the current position of the tail to the set of visited positions
      visited_positions.add((knots[-1][0], knots[-1][1]))

  # Return the number of unique positions the tail has visited
  return len(visited_positions)

# Read the series of motions from the input
motions = []
for line in open("91.txt").readlines():
  if line == '':
    break
  motions.append(line)

# Calculate the position of the tail
n_visited_positions = tail_position(motions)

# Print the number of unique positions visited by the tail
print(n_visited_positions)
