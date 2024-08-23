# easy

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

from typing import *
from unittest import TestCase
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        # First pass: count occurrences and store first index
        for i, char in enumerate(s):
            if char not in d:
                d[char] = [1, i]  # [count, first_index]
            else:
                d[char][0] += 1
        
        # Second pass: find the first unique character
        index_first_non_repeating = float('inf')
        for count, first_index in d.values():
            if count == 1:
                index_first_non_repeating = min(first_index, index_first_non_repeating)
        
        return index_first_non_repeating if index_first_non_repeating != float('inf') else -1

# test
t = TestCase()
s = Solution()
s.firstUniqChar("loveleetcode")