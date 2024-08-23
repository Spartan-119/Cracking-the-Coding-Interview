# easy

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from typing import *
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # first edge case
        if len(ransomNote) > len(magazine):
            return False
        
        # you will have to look at the char and their count/
        # they must match 
        ransomNote_dict = dict(Counter(ransomNote))
        magazine_dict = dict(Counter(magazine))

        for char in ransomNote_dict:
            if char not in magazine_dict: # checking the presence of the character
                return False
            else:
                # check the count is what we need
                if ransomNote_dict[char] > magazine_dict[char]:
                    return False
                
        return True
