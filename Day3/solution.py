from typing import NewType

def read_input():
    with open('input.txt') as file:        
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        # print(lines)

        return lines
read_input()

# need to store each spot and the most common int in spot
# essentially checking frequencies -> negative represents # of zeroes and positive is 1s
def most_common_bit():
    lines = read_input()

    # list with X slots that represents frequencies of bits at index
    bit_spot_to_most_common = []

    # initializing lists with length of input, could vary in text file
    for i in range(0, len(lines[0])):
        bit_spot_to_most_common.append(0)

    # this will give us a list where neg frequency means 0 is dominaant and 1 is pos is dom

    for i in range(0, len(lines)): # going thru list of binary #
        for j in range(0, len(lines[i])): # going thru actual binary #
            # case where we see a 0 in the binary #
            if int(lines[i][j]) == 0: 
                bit_spot_to_most_common[j] -= 1
            if int(lines[i][j]) == 1: 
                bit_spot_to_most_common[j] += 1
    print(bit_spot_to_most_common)

    gamma = ""
    epsilon = ""

    # convert frequency arrays to gamma (most common) and epsilon (least common)
    for i in range(0, len(bit_spot_to_most_common)):
        if bit_spot_to_most_common[i] < 0: # case where 0 was more frequent
            gamma += "0"
            epsilon += "1"
        if bit_spot_to_most_common[i] > 0: # case where 1 was more frequent
            gamma += "1"
            epsilon += "0"
    
    power_consumption = (int(gamma, 2)) * (int(epsilon, 2)) # convert from binary to dec and multiply for consumption rate
    print(power_consumption)

# most_common_bit()

# if ur reading this, sorry for the rabbit hole. this was my b...have a good day future self
### part 2 solution ###

############ most common bit at index given ############
def most_common_at_specific_bit(lines, bit_of_interest, version):
    most_common_bits = []
    teeter_totter = 0 # goes down when sees 0 and up when sees 1; ends at 0 if even split
    
    current_bit = 0
    index = 0
    done = False
    
    while done is not True:

        if (lines[index][bit_of_interest] is "0"): # checking current binary number's nth bit where n is # of letters
            teeter_totter -= 1
        else:
            teeter_totter += 1
        if index == len(lines) - 1:
            most_common_bits.append(teeter_totter)
          
        if index < len(lines) - 1:
            index += 1
        else:
            index = 0 # restart to top of list
            done = True

    # TWO CASES based on least and most common bit to get different rates for puzzle
    # translating to most common

    final_most_common = []
    if version is "LeastCommon":
        for i in range(0, len(most_common_bits)):
            if int(most_common_bits[i]) > 0: # more frequent zeroes case
                final_most_common.append(0)
            if int(most_common_bits[i]) == 0: # equally common case
                final_most_common.append(0)
            if int(most_common_bits[i]) < 0: # more frequent 1s
                final_most_common.append(1)
        return final_most_common[0]
    if version is "MostCommon":
        for i in range(0, len(most_common_bits)):
            if int(most_common_bits[i]) < 0: # more frequent zeroes case
                final_most_common.append(0)
            if int(most_common_bits[i]) == 0: # equally common case
                final_most_common.append(1)
            if int(most_common_bits[i]) > 0: # more frequent 1s
                final_most_common.append(1)
        return final_most_common[0]
    else:
        return ["Error occurred"]

def calculate_life_support_rating(verison):
    lines = read_input()
    lines_copy = lines.copy()

    current_bit = 0
    index = 0

    done = False
    while(done is not True):
        if (int(lines_copy[index][current_bit]) != most_common_at_specific_bit(lines_copy, current_bit, verison)):
            lines.remove(lines_copy[index])
        
        # have we reached the bottom?
        if index == len(lines_copy) - 1: # reached end of input (for single bit) i.e. column
            current_bit += 1

        # have we reached the right most bit?  
        if (current_bit == len(lines_copy[0]) or len(lines) == 1): # assuming all binary #s are same length and gone thru all bits
            done = True
        
        # case where we need to go to next row
        if index < len(lines_copy) - 1:
            index += 1
        else:
            index = 0 # restart to top of list
            lines_copy = lines.copy() # updating copied list to list that has removals as it goes  
    
    value = lines[0] # our answer is the final remaining value
    return value
    
def solution():
    CO_scrubber_rating = calculate_life_support_rating("LeastCommon")
    oxygen_generator_rating = calculate_life_support_rating("MostCommon")
    print(CO_scrubber_rating)
    print(oxygen_generator_rating)

    life_support_rating = int(CO_scrubber_rating, 2) * int(oxygen_generator_rating, 2)
    print(life_support_rating)
solution()