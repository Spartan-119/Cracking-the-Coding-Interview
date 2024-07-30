# medium

"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""

import unittest
from typing import *

# 1. BRUTE FORCE METHOD
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         def starts_with(root, word) -> bool:
#             return root == word[:len(root)]
        
#         result = []
#         words_list = sentence.split()

#         for word in words_list:
#             # need a flag
#             replaced = False
#             for root in dictionary:
#                 if starts_with(root, word):
#                     result.append(root)
#                     replaced = True
#                     break
#             if not replaced:
#                 result.append(word)

#         return " ".join(result)

# 2. TRIE
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_root(self, word):
        node = self.root
        root = ""
        for char in word:
            if char in node.children:
                root += char
                node = node.children[char]
                if node.is_end_of_word:
                    return root # return the root as soon as we fin it
            else:
                break
        return word # return the original word if no root is found

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build the Trie from the dictionary
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        # Split the sentence into words and replace them
        words_list = sentence.split()
        result = []

        for word in words_list:
            root = trie.search_root(word)
            result.append(root)

        return " ".join(result)
    
sol = Solution()
print(sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))