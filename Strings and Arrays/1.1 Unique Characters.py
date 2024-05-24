# Approach 1
def UniqueCharacters1(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False

    return True

##########################################
# Approach 2
def UniqueCharacters2(s):
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True


###########################################
# Approach 3:

MAX_CHAR = 256

def UniqueCharacters3(st):
    n = len(st)

    if n > MAX_CHAR:
        return False

    chars = [False] * MAX_CHAR

    for index in range(n):
        ''' if the value is already true,
        string has duplicate characters.
        return False '''
        val = ord(st[index])
        if chars[val]:
            return False

        chars[val] = True

    # No duplicate values => return true
    return True

########################################
# Approach 4

import math

def UniqueCharacters4(st):
    # assuming the string can have characters
    # a-z this has 32 bits set to 0

    checker = 0

    for i in range(len(st)):
        bitAtIndex = ord(st[i]) - ord('a')

        # if that bit is already set in the checker,
        # return False
        if (bitAtIndex) > 0:
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False

            # otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)

    return True



# testing the function
s1 = "dbacaeb"
s2 = "abin"

print(UniqueCharacters4(s1))
print(UniqueCharacters4(s2))