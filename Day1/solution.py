# Puzzle part 1
def read_input_file():
    with open('puzzle_input.txt') as file:
        return [int(i) for i in file.read().split("\n")]
        
read_input_file()

def num_depth_increases():
    input = read_input_file()
    total_increases = 0
    current_val = input[0]

    # start at second value (for comparison) 
    # and iterate to end
    for i in range(1, len(input)):
        if (current_val < input[i]):
            total_increases += 1

        # update value to next
        current_val = input[i]
    print(total_increases)

num_depth_increases()

# Puzzle part 2
def num_depth_increases_sliding_window():
    input = read_input_file()
    total_increases = 0

    first_val = input[0]
    second_val = input[1]
    third_val = input[2]
    curr_window = first_val + second_val + third_val

    for i in range(1, len(input)):
        # prevent out of bounds; our group/window is the last 3 index values
        if (i + 3) <= len(input):
            comparison_window = input[i] + input[i+1] + input[i+2]
            if curr_window < comparison_window:
                total_increases += 1
            curr_window = comparison_window
    print(total_increases)

num_depth_increases_sliding_window()

