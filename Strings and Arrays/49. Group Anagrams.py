# medium
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(word)
        
        return list(grouped.values())
    

# The issue with the test case `["", ""]` not passing in your original code is due to the way the intermediate dictionary `d` is constructed. Specifically, the keys in `d` are the original words, and the values are the sorted versions of those words. This approach can lead to problems when the original words are empty strings or when there are duplicate words.

# Let's revisit your original code and identify the problem:

# ### Your Original Code:
# ```python
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         def condense(word):
#             return "".join(sorted(word))
        
#         d = {}
#         for word in strs:
#             d[word] = condense(word)
        
#         grouped = {}
#         for key, val in d.items():
#             if val not in grouped:
#                 grouped[val] = []
#             grouped[val].append(key)
        
#         return list(grouped.values())
# ```

# ### Problem:
# - The dictionary `d` uses the original words as keys. When the words are empty strings or duplicates, this can lead to issues.
# - Specifically, with the input `["", ""]`, the dictionary `d` will only have one entry: `{"": ""}`, which means the second empty string will overwrite the first one.

# ### Solution:
# To fix this issue, we should directly use the sorted version of each word as the key in the `grouped` dictionary, without creating the intermediate dictionary `d`.

# ### Corrected Code:
# ```python
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         grouped = {}
#         for word in strs:
#             key = ''.join(sorted(word))
#             if key not in grouped:
#                 grouped[key] = []
#             grouped[key].append(word)
        
#         return list(grouped.values())
# ```

# ### Explanation:
# - This corrected code directly processes each word and updates the `grouped` dictionary.
# - The key for the `grouped` dictionary is the sorted version of each word, ensuring that anagrams are grouped together.
# - This approach handles empty strings and duplicate words correctly.

# ### Test Case:
# Let's test the corrected code with the input `["", ""]`:

# ```python
# # Example usage
# sol = Solution()
# print(sol.groupAnagrams(["", ""]))  # Output: [["", ""]]
# ```

# This should output `[['', '']]`, correctly grouping the empty strings together.

# ### Summary:
# The issue with your original code was the use of the original words as keys in the intermediate dictionary `d`. This approach can lead to problems with empty strings or duplicate words. The corrected code directly uses the sorted version of each word as the key in the `grouped` dictionary, which handles these cases correctly.