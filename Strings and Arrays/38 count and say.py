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

"""
Certainly! Here are the key lessons and notes from solving this "Count and Say" problem:

1. Problem Understanding:
   - Carefully read and understand the problem statement, especially for complex problems like this one.
   - Pay attention to how the Run-Length Encoding (RLE) is defined in the context of this specific problem.

2. RLE Implementation:
   - RLE counts consecutive identical characters, not all occurrences of a character in the string.
   - The count goes before the character in the encoded result (e.g., "111" becomes "31", not "13").

3. Edge Cases:
   - Remember to handle the last group of characters in the RLE function.
   - The line `res.append(str(count) + s[-1])` is crucial for including the last character group.

4. Testing:
   - Write comprehensive unit tests covering various scenarios.
   - Include edge cases like single characters, repeated characters, and mixed sequences.

5. Test Case Validation:
   - Double-check that your test cases align with the problem requirements.
   - In this case, the initial expectation for "1223334" was incorrect ("112233341" instead of "11223314").

6. Iterative vs Recursive:
   - The problem can be solved both recursively and iteratively. The given solution uses a recursive approach for `countAndSay` and an iterative approach for `RLE`.

7. String Processing:
   - Using a list to build the result and then joining it (`''.join(res)`) is often more efficient than string concatenation in a loop.

8. Code Structure:
   - Separating the RLE logic into its own method improves readability and maintainability.

9. Python-specific Notes:
   - Use `str()` to convert integers to strings when concatenating.
   - Remember that string indexing in Python allows negative indices (e.g., `s[-1]` for the last character).

10. Problem-Solving Approach:
    - Break down the problem into smaller parts (e.g., separating the counting logic from the recursive part).
    - Implement and test each part separately before combining them.

11. Debugging:
    - When tests fail, carefully compare the expected and actual outputs to identify the discrepancy.
    - Use print statements or a debugger to step through the code if necessary.

12. Time and Space Complexity:
    - Consider the efficiency of your solution, especially for larger inputs.
    - The current solution's time complexity grows with n, as each step builds on the previous one.

IMPORTANT:
### Handling the Last Group of Characters in RLE: Key Points

#### Why It's Important:
1. **Incomplete Processing**: The main loop processes characters up to the second-to-last character. Without handling the last group, the final characters may be missed.
2. **Accuracy**: Ensuring the last group is included is crucial for accurate encoding.
3. **Edge Cases**: Single-character strings or strings where the last character differs from the preceding ones need special handling.

#### How to Solve It:
1. **Append After the Loop**:
   - After the main loop, append the count and the last character to the result.
   - This ensures the last group of characters is included in the final encoded string.

2. **Why It Works**:
   - `count` retains the count of the last group of identical characters.
   - `s[-1]` accesses the last character of the string.

3. **Examples of Its Importance**:
   - For "aaa": Without handling the last group, the result would be incomplete.
   - For "aaab": The final "b" would be missed without special handling.

4. **Considerations**:
   - Ensure this step runs even for single-character strings.
   - Avoid double-counting or missing characters at the boundary.

By addressing this edge case, you ensure your RLE function is robust and handles all input scenarios correctly.
"""