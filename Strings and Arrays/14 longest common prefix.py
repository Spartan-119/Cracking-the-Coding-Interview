# 14. Longest common prefix [easy]

import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # here the reference string would be the shortest string.
        # because by definition, it will be the longest common prefix if 
        # the rest of the strings have it in them at the start.
        shortest = min(strs, key = len)

        for i in range(len(shortest)):
            char = shortest[i]
            # now I will run through each string
            for string in strs:
                if string[i] == char:
                    continue 
                else:
                    return shortest[: i]
        
        return shortest

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.longestCommonPrefix([]), "")

    def test_single_string(self):
        self.assertEqual(self.solution.longestCommonPrefix(["hello"]), "hello")

    def test_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_all_same_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["aa", "aa", "aa"]), "aa")

    def test_prefix_is_whole_string(self):
        self.assertEqual(self.solution.longestCommonPrefix(["ab", "abc", "abcd"]), "ab")

    def test_different_lengths(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a", "ab", "abc", "abcd"]), "a")

    def test_unicode_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["ünicode", "üni", "üniform"]), "üni")


if __name__ == "__main__":
    unittest.main()