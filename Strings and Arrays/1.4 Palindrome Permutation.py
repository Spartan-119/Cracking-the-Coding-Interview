'''
Given a string, write a function to check if it is a permutation of a palindrome.'''

# --------X-------X-------X-------X-------X-------X-------X-------X------- #
# Approach 1
def is_Permutation_of_Palindrome_approach_1(string):
    # first you will convert all characters to lowercase to
    # make the string effectively case insensitive
    string = string.lower()
    count = {}

    for i in string:
        # if you encounter a white space, ignore it and continue
        if i == " ":
            continue
        
        # here you are essentially creating a hash_function/dictionary 
        # and filling in this dictionary with the count of each character
        # in the string
        count[i] = count.get(i, 0) + 1
    
    # creating a flag
    hasOdd = False
    
    # Now you will apply the main logic
    for value in count.values():
        # in case the count is odd
        if value % 2 == 1:
            if hasOdd:
                # This is the case when we have
                # a character that appears an odd
                # number of time
                return False
            hasOdd = True
    
    return True


# --------X-------X-------X-------X-------X-------X-------X-------X------- #
# Approach 2
def is_Permutation_of_Palindrome_approach_2(string):
    pass

# --------X-------X-------X-------X-------X-------X-------X-------X------- #

# Testing this function

word = 'Tact Coa'
print(is_Permutation_of_Palindrome_approach_1(word))