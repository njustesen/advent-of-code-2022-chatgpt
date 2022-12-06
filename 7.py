# Part 1:

def find_start_of_packet_marker(buffer):
    # Initialize a counter to keep track of the number of characters processed
    num_chars_processed = 0

    # Iterate through the characters in the buffer
    for char in buffer:
        # Increment the counter for each character processed
        num_chars_processed += 1

        # Check if the last four characters are all different
        if len(set(buffer[num_chars_processed - 4:num_chars_processed])) == 4:
            # Return the number of characters processed if they are
            return num_chars_processed

    # Return -1 if no start-of-packet marker was found
    return -1


# Test the subroutine with the example input
buffer = open("7.txt").read()
print(find_start_of_packet_marker(buffer))


# Part 2:

def find_start_of_message_marker(buffer):
    # Initialize a counter to keep track of the number of characters processed
    num_chars_processed = 0

    # Iterate through the characters in the buffer
    for char in buffer:
        # Increment the counter for each character processed
        num_chars_processed += 1

        # Check if the last 14 characters are all different
        if len(set(buffer[num_chars_processed - 14:num_chars_processed])) == 14:
            # Return the number of characters processed if they are
            return num_chars_processed

    # Return -1 if no start-of-message marker was found
    return -1


# Test the subroutine with the example input
buffer = open("7.txt").read()
print(find_start_of_message_marker(buffer))  # Expected output: 19
