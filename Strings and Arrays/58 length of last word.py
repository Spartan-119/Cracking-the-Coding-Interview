"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

import unittest

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         # Trim trailing spaces and split the string
#         words = s.strip().split()
        
#         # If the string is empty after trimming, return 0
#         if not words:
#             return 0
        
#         # Return the length of the last word
#         return len(words[-1])


## however, in cases of extremely long strings, it doesn't make sense to use strip and all.
## instead traverse the string from the right and be done

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # skip all the trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # if the code execution has reached here, that means we're at the last word
        # count characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length

class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_last_word(self):
        # Test case 1: Normal case
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

        # Test case 2: Multiple spaces between words
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)

        # Test case 3: Single word
        self.assertEqual(self.solution.lengthOfLastWord("luffy"), 5)

        # Test case 4: Trailing spaces
        self.assertEqual(self.solution.lengthOfLastWord("a "), 1)

        # Test case 5: Empty string
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)

        # Test case 6: Only spaces
        self.assertEqual(self.solution.lengthOfLastWord("     "), 0)

if __name__ == '__main__':
    unittest.main()