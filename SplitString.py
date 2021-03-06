#         -- WHAT THIS SHOULD ACCOMPLISH --
# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def split_string(source, splitlist):
    # defines a function, split_string, that takes a string to be split and a list containing
    # all of the characters considered seperators.
    temp_list = []
    # defines a variable, containing an empty list
    current_digit = 0
    # defines a variable, named current_digit that is equal to the integer 0.
    for i in range(len(source)):
        # creates a loop that iterates over the list, of the range, of the length, of the source.
        if source[i] in splitlist:
            # if a character is equal to any values in the list 'splitlist':
            temp_list.append(source[current_digit:i])
            print temp_list
            # append to temp_list source at the location of the current digit and the current iteration.
            current_digit = i + 1
            # 
        if i == len(source) - 1 and i > current_digit:
            #
            temp_list.append(source[current_digit:i+1])
            #
    return_list = []
    # creates a variable called return_list, containing an empty list.
    for e in temp_list:
        # for each iteration in the list temp_list:
        if len(e) > 0:
            # if the length of the iteration is greater than 0:
            return_list.append(e)
            # append to the return_list the value of the iteration
    return return_list
    # return the value of return_list
    
out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
