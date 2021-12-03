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

    # represents epsilon rate
    bit_spot_to_least_common = []

    # initializing lists with length of input, could vary in text file
    for i in range(0, len(lines[0])):
        bit_spot_to_most_common.append(0)
        bit_spot_to_least_common.append(0)

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

most_common_bit()



# def binary_to_dec_helper(val):

