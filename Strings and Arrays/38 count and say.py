# medium
"""
 The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?
"""

import unittest
from typing import *

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        return self.RLE(prev)

    def RLE(self, s: str) -> str:
        if not s:
            return ""
        
        res = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res.append(str(count) + s[i - 1])
                count = 1
        
        # Add the last group
        res.append(str(count) + s[-1])
        
        return ''.join(res)

class TestCountAndSay(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_equals_1(self):
        self.assertEqual(self.solution.countAndSay(1), "1")

    def test_n_equals_2(self):
        self.assertEqual(self.solution.countAndSay(2), "11")

    def test_n_equals_3(self):
        self.assertEqual(self.solution.countAndSay(3), "21")

    def test_n_equals_4(self):
        self.assertEqual(self.solution.countAndSay(4), "1211")

    def test_n_equals_5(self):
        self.assertEqual(self.solution.countAndSay(5), "111221")

    def test_n_equals_6(self):
        self.assertEqual(self.solution.countAndSay(6), "312211")

    def test_n_equals_10(self):
        self.assertEqual(self.solution.countAndSay(10), "13211311123113112211")

    def test_RLE_single_char(self):
        self.assertEqual(self.solution.RLE("1"), "11")

    def test_RLE_repeated_chars(self):
        self.assertEqual(self.solution.RLE("111"), "31")

    def test_RLE_mixed_chars(self):
        self.assertEqual(self.solution.RLE("1223334"), "11223314")  # Corrected expected output

if __name__ == '__main__':
    unittest.main()