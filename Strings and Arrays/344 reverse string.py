# leetcode 344. reverse string

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

from typing import List
import unittest

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        # first edge case:
        if len(s) < 2:
            return s

        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
        return s

class TestReverseString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_reverse_string(self):
         # Test case 1: Even number of characters
        s1 = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s1)
        self.assertEqual(s1, ["o", "l", "l", "e", "h"])

        # Test case 2: Odd number of characters
        s2 = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s2)
        self.assertEqual(s2, ["h", "a", "n", "n", "a", "H"])

        # Test case 3: Single character
        s3 = ["a"]
        self.solution.reverseString(s3)
        self.assertEqual(s3, ["a"])

        # Test case 4: Empty list
        s4 = []
        self.solution.reverseString(s4)
        self.assertEqual(s4, [])

if __name__ == '__main__':
    unittest.main()